from django.shortcuts import render, HttpResponse


# Create your views here.
#Эта вьюха отвечает за отображение шаблона
def products(request):
    template = 'products/products.html'
    #return HttpResponse(f'Общий список товаров!') #Старый вариант!
    context = {
        'title': 'products'
    }
    return render(request, template, context)

def products_list(request, slug):
    template = 'products/products_list.html'
    #return HttpResponse(f'Конкретный товар {slug}') #Старый вариант!
    context = {
        'title': 'products_list'
    }
    return render(request, template, context)

