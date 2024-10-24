"""
URL configuration for arsens_toyboss_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from toyboss_factory.views import (HomePageView, ProductPageView, ProductDetailPageView,
                                   PublicationPageView, PublicationDetailPageView,
                                   AboutPageView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home-page-url'),
    path('products/', ProductPageView.as_view(), name='product-list-url'),
    path('products/<int:pk>/', ProductDetailPageView.as_view(), name='product-detail-url'),
    path('publications/', PublicationPageView.as_view(), name='publication-list-url'),
    path('publications/<int:pk>/', PublicationDetailPageView.as_view(), name='publication-detail-url'),
    path('about/', AboutPageView.as_view(), name='about-page-url'),
]
