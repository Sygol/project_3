# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.core.exceptions import ObjectDoesNotExist
# from django.http import JsonResponse, Http404
# from django.shortcuts import render, redirect
#
# # Create your views here.
# from django.urls import reverse_lazy
# from django.views.generic import ListView, TemplateView, DeleteView, UpdateView, CreateView
#
# from orders.forms import CartItemForm
# from orders.models import CartItem, Order, OrderStatusCode, OrderItem
# from pizza.models import ProductType, Product, SubExtra, Topping
#
#
# def check_price(request):
#     product_type_id = request.GET.get('product')
#     product_size = request.GET.get('size')
#     product_name = request.GET.get('name')
#     quantity = request.GET.get('quantity')
#     client_extra_price = sub_extra(request)
#
#     data = {
#         'price': (float(
#             Product.objects.filter(type=product_type_id, size=product_size, name=product_name).values_list(
#                 'price', flat=True)[0]) + client_extra_price) * float(quantity)}
#     return JsonResponse(data)
#
#
# def sub_extra(request):
#     client_extra_price = 0
#     if 'cheese' in request.GET:
#         cheese = request.GET.get('cheese')
#         extras = float(request.GET.get('sub_extra'))
#         extra_price = float(SubExtra.objects.filter(id=1).values_list('price', flat=True)[0])
#         if cheese == 'true':
#             client_extra_price += extra_price
#         if extras != 0.0:
#             client_extra_price += extras * extra_price
#     return client_extra_price
#
#
# class PizzaOrderView(LoginRequiredMixin, CreateView):
#
#     template_name = 'orders/pizza_order.html'
#     success_url = reverse_lazy('cart')
#     form_class = CartItemForm
#     login_url = '/login/'
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs.update({'request': self.request, 'product_type': 'Pizza'})
#         return kwargs
#
#
# class SubOrderView(LoginRequiredMixin, CreateView):
#     template_name = 'orders/sub_order.html'
#     success_url = reverse_lazy('cart')
#     form_class = CartItemForm
#     login_url = '/login/'
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs.update({'request': self.request, 'product_type': 'Sub'})
#         return kwargs
#
#
# class PastaOrderView(LoginRequiredMixin, CreateView):
#     template_name = 'orders/pasta_order.html'
#     success_url = reverse_lazy('cart')
#     form_class = CartItemForm
#     login_url = '/login/'
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs.update({'request': self.request, 'product_type': 'Pasta'})
#         return kwargs
#
#
# class SaladOrderView(LoginRequiredMixin, CreateView):
#     template_name = 'orders/salad_order.html'
#     success_url = reverse_lazy('cart')
#     form_class = CartItemForm
#     login_url = '/login/'
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs.update({'request': self.request, 'product_type': 'Salad'})
#         return kwargs
#
#
# class DinnerOrderView(LoginRequiredMixin, CreateView):
#     template_name = 'orders/dinner_order.html'
#     success_url = reverse_lazy('cart')
#     form_class = CartItemForm
#     login_url = '/login/'
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs.update({'request': self.request, 'product_type': 'Dinner'})
#         return kwargs
#
#
# class CartView(LoginRequiredMixin, ListView):
#     template_name = 'orders/cart.html'
#     login_url = '/login/'
#
#     def get_queryset(self):
#         return CartItem.objects.filter(user=self.request.user)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         price = 0
#         extra = SubExtra.objects.get(id=1)
#         for obj in context['object_list']:
#             price += obj.product.price * obj.quantity
#             if len(obj.extras.all()):
#                 price += extra.price * len(obj.extras.all()) * obj.quantity
#         context['price'] = price
#         return context
#
#     def post(self, request):
#         status_code = OrderStatusCode.objects.get(id=1)
#         user = request.user
#         order = Order.objects.create(user=user, status_code=status_code)
#         items_to_add = CartItem.objects.filter(user=user)
#
#         for item in items_to_add:
#             order_item = OrderItem.objects.create(
#                 order=order,
#                 product=item.product,
#                 quantity=item.quantity
#             )
#             if item.toppings.all():
#                 for topping in item.toppings.all():
#                     order_item.toppings.add(topping)
#             if item.extras.all():
#                 for extra in item.extras.all():
#                     order_item.extras.add(extra)
#
#         CartItem.objects.filter(user=user).delete()
#         return redirect('confirmation')
#
#
# class ConfirmationView(LoginRequiredMixin, TemplateView):
#     template_name = 'orders/confirmation.html'
#     login_url = '/login/'
#
#
# class ProductDeleteView(LoginRequiredMixin, DeleteView):
#     model = CartItem
#     success_url = reverse_lazy('cart')
#     login_url = '/login/'
#
#
# class ProductUpdateView(LoginRequiredMixin, UpdateView):
#     form_class = CartItemForm
#     model = CartItem
#     types = list(ProductType.objects.filter(name__contains='Pizza').values_list('id', flat=True))
#     success_url = reverse_lazy('cart')
#     login_url = '/login/'
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         item = CartItem.objects.get(pk=self.kwargs.get('pk'))
#         if item.product.type.id == 1 or item.product.type.id == 2:
#             kwargs.update({'request': self.request, 'product_type': 'Pizza'})
#         elif item.product.type.id == 3:
#             kwargs.update({'request': self.request, 'product_type': 'Sub'})
#         elif item.product.type.id == 4:
#             kwargs.update({'request': self.request, 'product_type': 'Pasta'})
#         elif item.product.type.id == 5:
#             kwargs.update({'request': self.request, 'product_type': 'Salad'})
#         elif item.product.type.id == 6:
#             kwargs.update({'request': self.request, 'product_type': 'Dinner'})
#         return kwargs
#
#     def get_template_names(self):
#         item = CartItem.objects.get(id=self.kwargs.get('pk'))
#         if item.product.type.id == 1 or item.product.type.id == 2:
#             self.template_name_suffix = '_pizza_update'
#         elif item.product.type.id == 3:
#             self.template_name_suffix = '_sub_update'
#         elif item.product.type.id == 4:
#             self.template_name_suffix = '_pasta_update'
#         elif item.product.type.id == 5:
#             self.template_name_suffix = '_salad_update'
#         elif item.product.type.id == 6:
#             self.template_name_suffix = '_dinner_update'
#         return super().get_template_names()
#
#     def get_initial(self):
#         item = CartItem.objects.get(pk=self.kwargs.get('pk'))
#         cheese_id = 4
#         initial = super().get_initial()
#         initial['product_sizes'] = item.product.size
#         initial['product_types'] = item.product.type
#         initial['product_names'] = item.product.name
#         initial['extra_cheese'] = cheese_id in item.extras.all().values_list('id', flat=True)
#         return initial
#
#
# class OrderView(LoginRequiredMixin, ListView):
#     template_name = 'orders/order_list.html'
#     login_url = '/login/'
#
#     def get_queryset(self):
#         return OrderItem.objects.filter(order__user=self.request.user).order_by('-order')