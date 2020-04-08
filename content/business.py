from content.utils.client import ContentClient
from dateutil.parser import parse
from random import shuffle

class Business:
    "Business class that that processes the request."
    
    def front_page(self): 
        """ Get the front data  """
        result = { 'title' : self.title_name("News and Analysis") }

        content = ContentClient() 
        data = content.latest()
        slug = '10-promise'
        story_count = 3
        
        result['front_story'] = self.get_headline(data['results'], slug) 
        result['stories'] = self.other_stories(data['results'], result['front_story'].uuid, story_count) 

        return result

    def get_headline(self, data, slug):
        """Get the top story that matches the slug """
        data =  list(filter(lambda a: any(map(lambda t: t['slug'] == slug , a['tags'])), data))

        result = Card(data[0])

        return result
    
    def get_article(self, category, year, month, day, title):
        result = { 'title' :  self.title_name("News and Analysis") }

        content = ContentClient() 
        data = content.get_article(category, year, month, day, title)
        latest = content.latest()
        article = Article(data)
        
        count = 5

        result['article'] = article 
        result['quotes'] = self.get_quotes(article) 
        result['links'] = self.other_stories(latest['results'], article.uuid, count) 
        
        return result

    def other_stories(self, data, uuid, count):
        """ Get count number of stories that are not the article""" 
        data =  list(filter(lambda a: a['uuid'] != uuid, data))
        result = self.take_cards(data, count)

        return result
    
    def take_cards(self, data, count):
        """ take n from a shuffled list  of items"""
        result = []

        shuffle(data)
        items = data[:count]
   
        for i in items:
            result.append(Card(i))

        return result

    def get_quotes(self, article):
        content = ContentClient() 
        quotes  = content.get_quotes(article.instruments())

        result = []
        for q in quotes:
            result.append(Quote(q))

        return result

    def title_name(self, name):
        result =  "Bufoncito | " + name 
        return result

class Quote:
    def __init__(self, quote):
        self.data = quote
        self.company_name = quote['CompanyName']
        self.exchange = quote['Exchange']
        self.symbol = quote['Symbol']
        self.current_price = quote['CurrentPrice']['Amount']
        self.price_change_amount = quote['Change']['Amount']
        self.price_change_percent = quote['PercentChange']['Value']
        
class Card:
    def __init__(self, story):
        self.uuid = story['uuid'] 
        self.headline = story['headline'] 
        self.promo = story['promo']
        self.images = story['images']
        self.date = parse(story['publish_at'])
        self.byline = story['byline']
        self.path = story['path']
        self.body = story['body'] 

class Article:
    def __init__(self, article):
        self.data = article
        self.uuid = article['uuid']
        self.headline = article['headline'] 
        self.byline = article['byline'] 
        self.published_at = parse(article['publish_at'])
        self.body = article['body'] 
        self.disclosure = article['disclosure'] 
        self.special_message = "Special Message" 
        self.pitch  = article['pitch']['text'] 

    def author_username(self):
        author = list(filter(lambda a: a['byline'] == self.byline, self.data['authors']))[0]

        return author['username']

    def instruments(self):
        result = list(map(lambda i: [i['exchange'], i['symbol']] , 
                    filter(lambda a: a['valid'] == True, 
                    self.data['instruments'])))

        return result
