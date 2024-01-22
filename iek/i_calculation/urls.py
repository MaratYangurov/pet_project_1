from django.urls import path, include
from . import views

urlpatterns = [
    path('i_calculation/', views.i_calculation, name='i_calculation'),
]