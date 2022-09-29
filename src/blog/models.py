
from unittest.util import _MAX_LENGTH
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()
    # category = models.ForeignKey(category, on_delete=models.PROTECT)
    published_date = models.DataTimeField(auto_now_add=True)
    last_uptaded = models.DataTimeField(auto_now=True)
    author 
    status draft published
    slug 

