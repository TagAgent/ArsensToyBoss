from django.db import models

class ProductCategory(models.Model):
    """Модель категории продукта"""
    name = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории товара'
        verbose_name = 'Категория товара'


class Product(models.Model):
    """Модель продукта"""
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    image = models.ImageField()

    class Meta:
        verbose_name_plural = 'Продукты'
        verbose_name = 'Продукт'


class Publication(models.Model):
    """Модель публикации"""
    title = models.CharField(max_length=150, verbose_name='Название')
    short_content = models.CharField(max_length=200, verbose_name='Краткое содержание')
    content = models.TextField(verbose_name='Содержание')

    preview_image = models.ImageField(upload_to='publication preview images')

    class Meta:
        verbose_name_plural = 'Публикации'
        verbose_name = 'Публикация'


class PublicationGallery(models.Model):
    """Модель галереи публикации"""
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='publication gallery images')

    class Meta:
        verbose_name_plural = 'Галереи публикации'
        verbose_name = 'Галерея товаров'

