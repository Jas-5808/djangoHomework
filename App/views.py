from django.shortcuts import render
from .models import *

# Create your views here.

def project_concept(request):
    concept = {'Target audience': 'Developers','Functional': 'web-dev','Distribution of content': 'main-home, about-about' ,'functionality across': 'main-site, about-site', 'Design': 'boostap' }
    return render(request, 'Pages/index.html', {'concept': concept})
def books_store(request):
    book = {'books': Book.objects.all()}
    return render(request, 'Pages/bookStore.html', {'book': book})