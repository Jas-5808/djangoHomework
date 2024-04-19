from django.contrib import admin
from .models import Book, Rent, Client

admin.site.register(Book)
admin.site.register(Rent)
admin.site.register(Client)

