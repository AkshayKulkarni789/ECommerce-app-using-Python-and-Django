from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Books
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
@login_required(login_url="accounts:login")
def booklist(request):
	books = Books.objects.all().order_by('price')
	return render(request, 'Books/book_list.html',{'books':books})

@login_required(login_url="accounts:login")
def book_details(request, slug):
	book = Books.objects.get(slug = slug)
	return render(request, 'Books/book_details.html',{'book':book})


@login_required(login_url="accounts:login")
def add_book(request):
	if request.method == 'POST':
		form = forms.CreateBook(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'Books/addbook.html',{'form':form})
	else:
		form = forms.CreateBook()
	return render(request, 'Books/addbook.html',{'form':form})