from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    # articles: related field for Article.categories
    # resources: related field for Resource.categories


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User)
    text = models.TextField()
    categories = models.ManyToManyField(Category, related_field='articles')


class Resource(models.Model):
    '''
    A resource for users, such as lawyers' offices, domestic violence shelters, tenants' groups, etc.
    '''
    name = models.CharField(max_length=50)
    description = models.TextField()
    address = models.TextField()
    phone = models.CharField(max_length=20)
    hours = models.TextField()
    categories = models.ManyToManyField(Category, related_field='resources')
