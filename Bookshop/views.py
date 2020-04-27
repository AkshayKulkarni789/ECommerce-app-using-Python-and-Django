from django.shortcuts import render
from Books import forms

def homepage(request):
	return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')
