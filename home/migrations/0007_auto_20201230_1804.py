# Generated by Django 3.1 on 2020-12-30 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20201230_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='products',
        ),
        migrations.CreateModel(
            name='OrderAdminPanel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.customer')),
                ('orders', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.orderitem')),
            ],
        ),
    ]
