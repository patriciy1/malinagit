# Generated by Django 3.1 on 2021-01-19 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20210120_0142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='cash_payment',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='robokassa_payment',
        ),
    ]
