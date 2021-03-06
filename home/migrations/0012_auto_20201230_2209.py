# Generated by Django 3.1 on 2020-12-30 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20201230_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderadminpanel',
            name='address',
            field=models.CharField(default='address', max_length=500),
        ),
        migrations.AddField(
            model_name='orderadminpanel',
            name='address_2',
            field=models.CharField(default='address_2', max_length=500),
        ),
        migrations.AddField(
            model_name='orderadminpanel',
            name='cash_payment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderadminpanel',
            name='company',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='orderadminpanel',
            name='company_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='orderadminpanel',
            name='consent',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='orderadminpanel',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='orderadminpanel',
            name='email',
            field=models.CharField(default='email', max_length=500),
        ),
        migrations.AddField(
            model_name='orderadminpanel',
            name='name_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='orderadminpanel',
            name='note',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='orderadminpanel',
            name='phone',
            field=models.CharField(default='phone', max_length=15),
        ),
        migrations.AddField(
            model_name='orderadminpanel',
            name='phone_2',
            field=models.CharField(default='phone_2', max_length=15),
        ),
        migrations.AddField(
            model_name='orderadminpanel',
            name='question',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='orderadminpanel',
            name='robokassa_payment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderadminpanel',
            name='sec_name_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='orderadminpanel',
            name='orders',
            field=models.ManyToManyField(to='home.OrderItem'),
        ),
    ]
