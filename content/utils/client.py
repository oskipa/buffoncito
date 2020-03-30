# ServicesClient
# An business object that interfaces between the services apis and the site
# It will start simulating the calls, but then move to making them
import json

class ContentClient:
    def __init__(self):
        self.content = "content/utils/content_api.json"
        self.quotes = "content/utils/quotes_api.json"

    def latest(self): 
        with open(self.content) as f:
            data = f.read()
        result = json.loads(data) 
        return result
