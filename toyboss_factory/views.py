from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Product, ProductCategory


class HomePageView(TemplateView):
    template_name = 'index.html'


class ProductPageView(TemplateView):
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        context = {
            'product_categories': ProductCategory.objects.prefetch_related('products').all(),
        }
        return context


class ProductDetailPageView(TemplateView):
    template_name = 'product-inner.html'


class PublicationPageView(TemplateView):
    template_name = 'publications.html'


class PublicationDetailPageView(TemplateView):
    template_name = 'publications-inner.html'


class AboutPageView(TemplateView):
    template_name = 'about-company.html'
