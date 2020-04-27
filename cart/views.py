from django.shortcuts import render, redirect

from .models import cart
from Books.models import Books

def cartview(request):
	carts = cart.objects.filter(user_name=request.user)
	return render(request,'cart/cartview.html',{'carts':carts})

def addtocart(request, id):
	book = Books.objects.get(id=id)
	c = cart.objects.create(user_name=request.user, book_name=book)
	return redirect('/books/')

def purchase(request):
	total = 0
	carts = cart.objects.filter(user_name=request.user)
	for item in carts:
		total = total + item.book_name.price
	totals = total
	return render(request,'cart/billing.html',{'carts':carts , 'totals':totals})