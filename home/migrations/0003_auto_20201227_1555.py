# Generated by Django 3.1 on 2020-12-27 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20201227_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='banket_delivery',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='category',
            name='children_delivery',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='category',
            name='complex_delivery',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='category',
            name='menu_friday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='category',
            name='menu_thursday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='category',
            name='menu_tuesday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='category',
            name='menu_wednesday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='category',
            name='vip_delivery',
            field=models.BooleanField(default=False),
        ),
    ]
