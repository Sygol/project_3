from django import forms


from orders.models import CartItem
from orders.scripts import create_all_additions, update_all_additions
from pizza.models import ProductType, Product, Size, Topping, SubExtra


class CartItemForm(forms.ModelForm):
    product_types = forms.ModelChoiceField(queryset=ProductType.objects.none(), required=False)
    product_sizes = forms.ModelChoiceField(queryset=Size.objects.none(), required=False)
    product_names = forms.ChoiceField(choices=[('', '---------')])
    toppings = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Topping.objects.all(),
                                              required=False)
    extras = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=SubExtra.objects.exclude(
                                            name='Cheese'), required=False)
    extra_cheese = forms.BooleanField(required=False)

    class Meta:
        model = CartItem
        fields = ['product_types', 'product_names', 'product_sizes', 'toppings', 'extras', 'extra_cheese', 'quantity']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        # sent from views (kwargs.update)
        self.product_type = kwargs.pop('product_type', None)
        self.product_names_query = Product.objects.filter(type__name__contains=self.product_type).values_list(
            'name', flat=True).distinct()
        self.product_names_choices = [('', '---------')] + [(name, name) for name in self.product_names_query]
        self.is_object_created = kwargs['instance']
        super().__init__(*args, **kwargs)
        self.fields['product_types'].queryset = ProductType.objects.filter(name__contains=self.product_type)
        self.fields['product_sizes'].queryset = Size.objects.exclude(name='No size specified')
        self.fields['product_names'].choices = self.product_names_choices

        for fieldname in ['product_types', 'product_sizes', 'product_names', 'quantity']:
            self.fields[fieldname].widget.attrs['class'] = 'form-control'

        self.fields['quantity'].widget.attrs['value'] = 1
        self.fields['quantity'].widget.attrs['min'] = 1
        self.fields['quantity'].widget.attrs['max'] = 30

        if self.product_type == 'Pizza':
            self.fields['product_types'].widget.attrs['required'] = True

        if self.product_type != 'Pasta' or self.product_type != 'Salad':
            self.fields['product_sizes'].widget.attrs['required'] = True

    def save(self, commit=True):
        no_size_id = 3

        if self.product_type == 'Pizza':
            product = Product.objects.get(name=self.cleaned_data.get('product_names'), type=self.cleaned_data.get(
                        'product_types'), size=self.cleaned_data.get('product_sizes'))
        elif self.product_type == 'Pasta' or self.product_type == 'Salad':
            product = Product.objects.get(name=self.cleaned_data.get('product_names'), type=ProductType.objects.get(
                name__contains=self.product_type), size=no_size_id)
        else:
            product = Product.objects.get(name=self.cleaned_data.get('product_names'), type=ProductType.objects.get(
                name__contains=self.product_type), size=self.cleaned_data.get('product_sizes'))

        if not self.is_object_created:
            user_product = CartItem.objects.create(user_id=self.request.user.id, product=product,
                                                   quantity=self.cleaned_data.get('quantity'))
            create_all_additions(user_product, self.cleaned_data)
            return user_product

        else:
            CartItem.objects.filter(id=self.is_object_created.id).update(product=product,
                                                                         quantity=self.cleaned_data.get('quantity'))
            user_product = CartItem.objects.filter(id=self.is_object_created.id)
            update_all_additions(self.is_object_created.id, self.cleaned_data)
            return user_product
