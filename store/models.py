from __future__ import unicode_literals

from django.db import models
from django.db.models import ImageField

from cornelshop.settings import MEDIA_ROOT

import os


def get_image_path(instance, filename):
    return 'img/product.jpg'


class Product(models.Model):
    product_name=models.CharField(max_length=900)
    product_image = models.ImageField(upload_to=get_image_path, null=True)
    product_price=models.FloatField(max_length=10)
    product_discaunt=models.CharField(max_length=5, blank=True)
    product_category=models.CharField(max_length=1000)
    product_discription=models.TextField(max_length=1000)


    def __unicode__(self):
        return self.product_discription

    def __unicode__(self):
        return self.product_category


    def __unicode__(self):
        return self.product_name

    def image_img(self):
        if self.product_image:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.product_image.url)
        else:
            return '(no picture)'
    image_img.short_description = 'Picture'
    image_img.allow_tags = True

    class Meta:
        verbose_name='Product'
        verbose_name_plural='Products'
        ordering= ('product_name',)
