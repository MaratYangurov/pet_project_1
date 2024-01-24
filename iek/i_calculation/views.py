from django.shortcuts import render, HttpResponse

# Create your views here.
#Эта вьюха отвечает за отображение шаблона
def i_calculation(request):
    template = 'i_calculation/i_calculation.html'
    #return HttpResponse(f'Расчет токов и выбор АВ!') #Старый вариант!
    context = {
        'title': 'i_calculation'
    }
    return render(request, template, context)