from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.booklist, name='booklist'),
    path('<slug:slug>/', views.book_details, name='details'),
    path('add/', views.add_book, name='addbook'),
]
