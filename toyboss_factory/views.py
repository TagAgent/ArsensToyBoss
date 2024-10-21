from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'index.html'

class ProductPageView(TemplateView):
    template_name = 'product.html'

class ProductDetailPageView(TemplateView):
    template_name = 'product-inner.html'
