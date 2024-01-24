from django.shortcuts import render, HttpResponse


# Create your views here.
#Эта вьюха отвечает за отображение шаблона index.html
def index(request):
    template = 'index/index.html'
    #return HttpResponse('Главная страница!') #Старый вариант!

    context = {
        'title': 'index',
    }
    return render(request, template, context)

