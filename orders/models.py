from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.
from pizza.models import SubExtra


class OrderStatusCode(models.Model):
    name = models.CharField(max_length=32, verbose_name=_('Name'))
    created = models.DateTimeField(editable=False, default=timezone.now())
    modified = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(OrderStatusCode, self).save(*args, **kwargs)


class Order(models.Model):
    user = models.ForeignKey('accounts.CustomUser', related_name='orders', on_delete=models.CASCADE, verbose_name='User')
    status_code = models.ForeignKey('orders.OrderStatusCode', related_name='orders', on_delete=models.CASCADE, verbose_name=_("Status Code"))
    description = models.TextField(max_length=256, blank=True, null=True, verbose_name=_('Description'))
    created = models.DateTimeField(editable=False, default=timezone.now())
    modified = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'{self.user} - {self.status_code}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Order, self).save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey('orders.Order', related_name='order_items', on_delete=models.CASCADE, verbose_name=_('Order'))
    product = models.ForeignKey('pizza.Product', related_name='order_items', on_delete=models.CASCADE, verbose_name=_('Product'))
    quantity = models.SmallIntegerField(verbose_name=_('Quantity'))
    toppings = models.ManyToManyField('pizza.Topping', related_name='order_items', blank=True)
    extras = models.ManyToManyField('pizza.SubExtra', related_name='order_items', blank=True)
    created = models.DateTimeField(editable=False, default=timezone.now())
    modified = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'{self.quantity} of {self.product}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(OrderItem, self).save(*args, **kwargs)


class CartItem(models.Model):
    user = models.ForeignKey('accounts.CustomUser', related_name='carts', on_delete=models.CASCADE, verbose_name='User')
    product = models.ForeignKey('pizza.Product', related_name='carts', on_delete=models.CASCADE, verbose_name=_('Product'))
    quantity = models.SmallIntegerField(verbose_name=_('Quantity'))
    toppings = models.ManyToManyField('pizza.Topping', related_name='cart_items', blank=True)
    extras = models.ManyToManyField('pizza.SubExtra', related_name='cart_items', blank=True)
    created = models.DateTimeField(editable=False, default=timezone.now())
    modified = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'{self.quantity} of {self.product}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(CartItem, self).save(*args, **kwargs)

    def total_price(self):
        extra = SubExtra.objects.get(id=1)
        price = (self.product.price * self.quantity) + len(self.extras.all()) * extra.price * self.quantity
        return price
