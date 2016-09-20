# -*- coding:utf-8 -*-

from django.views.generic import DetailView, ListView
from .models import Product
from .forms import ProductlistForm

from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class ProductDitail(DetailView):
    template_name='product/product_detail.html'
    model=Product


class ProductList(ListView):
    template_name='product/product_list.html'
    model=Product

    def dispatch(self, request, *args, **kwargs):
        self.form = ProductlistForm(request.GET)
        self.form.is_valid()
        return super(ProductList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset=Product.objects.all()
        if self.form.cleaned_data['search']:
            queryset=queryset.filter(product_category=self.form.cleaned_data['search'])
        if self.form.cleaned_data['sort_field']:
            queryset=queryset.order_by(self.form.cleaned_data['sort_field'])
        return queryset

    def get_context_data(self, **kwargs):
        context=super(ProductList, self).get_context_data(**kwargs)
        context['form']=self.form
        return context




