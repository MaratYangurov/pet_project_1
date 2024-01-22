from django.shortcuts import render, HttpResponse


# Create your views here.
def products(request):
    return HttpResponse(f'Общий список товаров!')

def products_list(request, slug):
    return HttpResponse(f'Конкретный товар {slug}')

