from django.contrib import admin

from .models import Product, ProductCategory

# Register your models here.

class PostAdmin_Product(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('articl', 'description_product', 'i_nom', 'polus', 'voltage_nom', 'category', 'author',)
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('description_product',)
    # Добавляем возможность фильтрации
    list_filter = ('i_nom', 'polus', 'voltage_nom',)
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка
    empty_value_display = '-пусто-'

class PostAdmin_ProductCategory(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('name_category', 'description_category',)
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('description_category',)
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка
    empty_value_display = '-пусто-'


admin.site.register(Product, PostAdmin_Product)
admin.site.register(ProductCategory, PostAdmin_ProductCategory)

