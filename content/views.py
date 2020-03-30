from django.shortcuts import render
from .business import Business 

# Create your views here.

def index(request): 
    business = Business()
    front_page = business.front_page()

    return render(request, "content/index.html", front_page)
