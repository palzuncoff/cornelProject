# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-15 14:23
from __future__ import unicode_literals

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_auto_20160915_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='/img/tovar.jpg', null=True, upload_to=store.models.get_image_path),
        ),
    ]
