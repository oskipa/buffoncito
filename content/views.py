from django.shortcuts import render
from content.utils.client import ServicesClient 

# Create your views here.

def index(request): 
    client = ServicesClient() 
    data = client.latest_content()
    print("the length " + str(len(data['results'])))
    print("the keys " + ','.join(data['results'][0].keys()))
    selected = list(filter(lambda a: any(map(lambda t: t['slug'] == '10-promise' , a['tags'])), data['results']))

    return render(request, "content/index.html", {'title': 'Bufoncito News and Analysis | The multicolored Bufoncito', 'content': selected[0] })
