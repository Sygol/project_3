from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.


class ProductType(models.Model):
    name = models.CharField(max_length=32, verbose_name=_('Name'))
    created = models.DateTimeField(editable=False, default=timezone.now())
    modified = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(ProductType, self).save(*args, **kwargs)


class Size(models.Model):
    name = models.CharField(max_length=64, verbose_name=_('Name'))
    created = models.DateTimeField(editable=False, default=timezone.now())
    modified = models.DateTimeField(default=timezone.now())

    def __str__(self):
        if self.name == 'No size specified':
            return '-'
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Size, self).save(*args, **kwargs)


class Topping(models.Model):
    name = models.CharField(max_length=64, verbose_name=_('Name'))
    created = models.DateTimeField(editable=False, default=timezone.now())
    modified = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Topping, self).save(*args, **kwargs)


class SubExtra(models.Model):
    name = models.CharField(max_length=64, verbose_name=_('Name'))
    price = models.DecimalField(max_digits=4, decimal_places=2, verbose_name=_('Price'))
    created = models.DateTimeField(editable=False, default=timezone.now())
    modified = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(SubExtra, self).save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=64, verbose_name=_('Name'))
    type = models.ForeignKey('pizza.ProductType', related_name='pizza', on_delete=models.CASCADE, verbose_name=_('Type'))
    size = models.ForeignKey('pizza.Size', related_name='pizza', on_delete=models.CASCADE, verbose_name=_('Size'))
    price = models.DecimalField(max_digits=4, decimal_places=2, verbose_name=_('Price'))
    created = models.DateTimeField(editable=False, default=timezone.now())
    modified = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'{self.type}, {self.name}, size:{self.size}, {self.price}$'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Product, self).save(*args, **kwargs)


