from django.db import models
from django.contrib.auth.models import User
from Books.models import Books

# Create your models here.
class cart(models.Model):
	user_name = models.ForeignKey(User,default=None, on_delete=models.SET_DEFAULT)
	book_name = models.ForeignKey(Books,default=None, on_delete=models.SET_DEFAULT)