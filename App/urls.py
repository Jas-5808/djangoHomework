from django.urls import path
from App.views import *

urlpatterns = [
    path('', project_concept, name='project_concept'),
    path('booksStore/', books_store, name='store'),
]