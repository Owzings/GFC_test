from django.http import HttpResponse
from django.shortcuts import render, redirect
from GFC_test.models import Article
from GFC_test.forms import ArticleForm


def list_view(request): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # add the dictionary during initialization 
    context["dataset"] = Article.objects.all() 
          
    return render(request, "liste.html", context) 


def articles(request): 
    context ={} 
  
    form = ArticleForm(request.POST or None) 
    if form.is_valid(): 
        form.save() 
          
    context['form']= form 
    return render(request, "index.html", context) 