from calendar import month
from re import search

from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import ProductCategory, Product, Publication, PublicationGallery

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    def preview_image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return 'Нет изображения'


class PublicationGalleryInLineAdmin(admin.StackedInline):
    model = PublicationGallery
    extra = 1


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

    inlines = [PublicationGalleryInLineAdmin]
