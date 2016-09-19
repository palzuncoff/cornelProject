from django import forms

class ProductlistForm(forms.Form):

    search = forms.CharField(required=False)
    sort_field= forms.ChoiceField(choices=(('product_category', 'category'), ('product_price', 'price')), required=False)