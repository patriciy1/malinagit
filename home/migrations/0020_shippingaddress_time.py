# Generated by Django 3.1 on 2021-01-20 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20210120_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
