from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default = 'default.jpg', blank= True)
    author = models.ForeignKey(User, on_delete = models.CASCADE , default = None)

    def __str__(self):
        return self.title

    #this is created so as to return only a part of the article an the article list page
    def snippet(self):
        return self.body[:250] + "..."