# ServicesClient
# An business object that interfaces between the services apis and the site
# It will start simulating the calls, but then move to making them
import json

class ContentClient:
    def __init__(self):
        self.content = "content/utils/content_api.json"
        self.quotes = "content/utils/quotes_api.json"

    # Simulation of rest calls
    def read_content(self):
        with open(self.content) as f:
            data  = f.read()
        result = json.loads(data) 
        return result
    
    def read_quotes(self):
        with open(self.quotes) as f:
            data  = f.read()
        result = json.loads(data) 
        return result
   
    def quotes_get(self, path,  params):
        data = self.read_quotes()
        exchange, symbol = params
        query = list(
                filter (lambda q: q['Exchange'] == exchange and q['Symbol'] == symbol, 
                data)) 
        result = query[0]
        return result
         
    def content_get(self, request, params):
        if request == "/latest":
           return self.read_content()
        if request == "/article":
           return self.retrieve_article(params)

    def retrieve_article(self, params):
        raw = self.read_content()  
        data = raw['results']
        path = f"/{params['category']}/{params['year']}/{params['month']}/{params['day']}/{params['title']}.aspx"

        articles =  list(filter(lambda a: a['path'] == path, data))
        result = None
   
        if len(articles) > 0:
            result = articles[0]

        return result

    ### Public Interface

    def latest(self): 
        result = self.content_get("/latest", {})
        return result

    def get_article(self, category, year, month, day, title):
        params = {
            'category' : category,        
            'year' : year,        
            'month' : month,        
            'day' : day,        
            'title' : title,        
        }

        result = self.content_get("/article", params)
        return result

    def get_quotes(self, instruments):
        result = [] 
        for i in instruments:
         quote = self.quotes_get("/quote", i)
         result.append(quote)    

        return result
