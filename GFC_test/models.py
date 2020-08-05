from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    author = models.CharField(max_length=200)
    created = models.DateTimeField('date de creation')
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
    
class Author(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateTimeField('date de creation')
    langage = models.CharField(max_length=200)
    