# Generated by Django 3.1 on 2021-01-19 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20210120_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='cash_payment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='robokassa_payment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='sec_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
