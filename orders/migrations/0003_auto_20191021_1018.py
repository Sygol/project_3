# Generated by Django 2.2.6 on 2019-10-21 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20191021_0943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='price',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='price',
        ),
    ]
