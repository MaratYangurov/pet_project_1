from django.urls import path, include
from . import views

#namespace
app_name = 'i_calculation'

urlpatterns = [
    path('i_calculation/', views.i_calculation, name='i_calculation'),
]