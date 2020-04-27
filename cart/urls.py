from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'cart'

urlpatterns = [
	path('', views.cartview, name='cartview'),
	path('add/<int:id>/', views.addtocart, name='addtocart'),
	path('purchase/', views.purchase, name='billing'),
]