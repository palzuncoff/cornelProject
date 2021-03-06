# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-12 08:02
from __future__ import unicode_literals

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=900)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to=store.models.get_image_path)),
                ('product_price', models.FloatField(max_length=10)),
                ('product_discaunt', models.CharField(max_length=5)),
                ('product_category', models.CharField(max_length=100)),
                ('product_discription', models.TextField(max_length=1000)),
            ],
            options={
                'ordering': ('product_price',),
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
