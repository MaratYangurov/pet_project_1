from django.shortcuts import render, HttpResponse
from .models import Product

# Create your views here.
#Эта вьюха отвечает за отображение шаблона
def products(request):
    template = 'products/products.html'
    #return HttpResponse(f'Общий список товаров!') #Старый вариант!

    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    products_modular_av = Product.objects.all
    context = {
        'title': 'products',
        'products_modular_av': products_modular_av,
    }
    return render(request, template, context)

def products_list(request, slug):
    template = 'products/products_list.html'
    #return HttpResponse(f'Конкретный товар {slug}') #Старый вариант!
    context = {
        'title': 'products_list'
    }
    return render(request, template, context)

