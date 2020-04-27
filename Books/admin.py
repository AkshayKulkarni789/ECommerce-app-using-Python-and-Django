from django.contrib import admin
from .models import Books

class BooksAdmin(admin.ModelAdmin):
    #list_display = ('title', 'author','genre','descreption','price',)
    prepopulated_fields = {'slug':('title',)}
admin.site.register(Books, BooksAdmin)