from django.urls import path, include
from . import views

urlpatterns = [
    path('products/', views.products, name='products'),
    path('products/<slug:slug>/', views.products_list, name='products_list'),
]
