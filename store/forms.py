# -*- coding:utf-8 -*-

from django import forms

class ProductlistForm(forms.Form):

    search = forms.CharField(required=False)
    sort_field= forms.ChoiceField(choices=(('product_category', 'category'), ('product_price', 'price')), required=False)

    def clean(self):
        raise forms.ValidationError('sorry samthing is wrong')
