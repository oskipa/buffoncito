from django.db import models

# Create your models here.

class Comment(models.Model):
    article_id = models.CharField(max_length=100)
    content    = models.TextField()


class Settings(models.Model):
    setting = models.CharField(max_length=100)
    value   = models.CharField(max_length=100) 

