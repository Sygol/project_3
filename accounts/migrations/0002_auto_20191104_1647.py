# Generated by Django 2.2.6 on 2019-11-04 15:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 4, 15, 46, 59, 751953, tzinfo=utc), editable=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 4, 15, 46, 59, 751953, tzinfo=utc)),
        ),
    ]
