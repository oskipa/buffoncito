from content.utils.client import ContentClient
import re

class Business:
    "Business class that that processes the request."
    
    def front_page(self): 
        """ Get the front data  """
        result = { 'title' :"Bufoncito | News and Analysis" }

        content = ContentClient() 
        data = content.latest()
        slug = '10-promise'
        story_count = 3
        
        result['front_story'] = self.get_headline(data['results'], slug) 
        result['stories'] = self.get_stories(data['results'], slug, story_count) 

        return result

    def get_headline(self, data, slug):
        """Get the top story that matches the slug """
        data =  list(filter(lambda a: any(map(lambda t: t['slug'] == slug , a['tags'])), data))
        first = data[0]

        result = FrontStory(
                first['uuid'], 
                first['headline'], 
                first['body'],
                first['images'])

        return result

    def get_stories(self, data, slug, count):
        """ Get count number of stories that are not in the slug """
        result = []
        data =  list(filter(lambda a: any(map(lambda t: t['slug'] != slug , a['tags'])), data))

        stories = data[:count]
   
        for s in stories:
            result.append(Article( s['uuid'], 
            s['headline'], 
            s['body'],
            s['images']))

        return result


class Article:
    def __init__(self, uuid, headline, body, images):
        self.uuid = uuid 
        self.headline = headline 
        self.body = body 
        self.images = images 

    def teaser(self, length=600):
        """Returns a teaser of a certain length """
        text = self.body[:length]
        words = text.split(' ')
        words.pop()
        
        if not re.match(r"[.!?]", words[-1]):
            words[-1] = re.sub(r"[,:;]", '',words[-1])
            words[-1] = words[-1] + "..."    

        result = " ".join(words)

        return result

class FrontStory(Article):
    def __init__(self, uuid, headline, body, images):
        super().__init__(uuid, headline, body, images)
        
    def teaser(self):
        return super().teaser(900)    
