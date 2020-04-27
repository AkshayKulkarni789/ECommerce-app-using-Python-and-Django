from django import forms
from . import models

class CreateBook(forms.ModelForm):
	class Meta:
		model = models.Books
		fields = ['title','author','genre','description','price']