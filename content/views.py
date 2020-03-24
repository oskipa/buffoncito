from django.shortcuts import render

# Create your views here.

def index(request): 
    # get content from api
    # 
    return render(request, "content/index.html", {'title': 'Buffoncito News and Analysis | The multicolored Buffoncito', 'content': 'some content here' })
