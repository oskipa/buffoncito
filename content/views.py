from django.shortcuts import render
from .business import Business 

# Create your views here.

def index(request): 
    business = Business()
    front_page = business.front_page()

    return render(request, "content/index.html", front_page)

def article(request, category, year, month, day, title):
    business = Business()
    article = business.get_article(category, year, month, day, title)

    return render(request, "content/article.html", article)
