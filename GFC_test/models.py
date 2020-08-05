from django.db import models


class Article(models.Model):
    author = models.CharField(max_length=200)
    created = models.DateTimeField('date de creation')
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    