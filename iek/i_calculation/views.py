from django.shortcuts import render, HttpResponse

# Create your views here.
def i_calculation(request):
    return HttpResponse(f'Расчет токов и выбор АВ!')