from django.shortcuts import render, redirect
from .business import Business 
from .models import Comment 

# Create your views here.

def index(request): 
    business = Business()
    front_page = business.front_page()

    return render(request, "content/index.html", front_page)

def article(request, category, year, month, day, title):
    business = Business()
    article = business.get_article(category, year, month, day, title)

    article['category'] = category
    article['year'] = year
    article['month'] = month
    article['day'] = day
    article['title'] = title

    return render(request, "content/article.html", article)

def comment(request):
    uuid = request.POST['uuid']
    comment = request.POST['comment']
    url = request.POST['url']
    
    if len(comment) > 0:
        c = Comment(article_id=uuid, content=comment)
        c.save()
    
    return redirect(url) 
