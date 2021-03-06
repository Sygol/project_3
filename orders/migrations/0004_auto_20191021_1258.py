# Generated by Django 2.2.6 on 2019-10-21 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pizza', '0001_initial'),
        ('orders', '0003_auto_20191021_1018'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.SmallIntegerField(verbose_name='Quantity')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='pizza.Product', verbose_name='Product')),
                ('toppings', models.ManyToManyField(blank=True, related_name='cart_items', to='pizza.Topping')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.AddField(
            model_name='orderitem',
            name='toppings',
            field=models.ManyToManyField(blank=True, related_name='order_items', to='pizza.Topping'),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
