from django.http import HttpResponse
from django.shortcuts import render, redirect
from GFC_test.models import Article
from GFC_test.forms import ArticleForm
from django.shortcuts import (get_object_or_404, 
                              render, 
                              HttpResponseRedirect) 



def delete_view(request, id): 
    context ={} 
  
    obj = get_object_or_404(Article, id = id) 
  
  
    if request.method =="POST": 
        obj.delete() 
        return HttpResponseRedirect("/") 
  
    return render(request, "delete_view.html", context) 



def detail_view(request, id): 
    context ={} 
   
    context["data"] = Article.objects.get(id = id) 
           
    return render(request, "detail.html", context) 

def update_view(request, id): 
    context ={} 
  
    obj = get_object_or_404(Article, id = id) 
  
    form = ArticleForm(request.POST or None, instance = obj) 
  
    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect("/"+id) 
  
    context["form"] = form 
  
    return render(request, "update.html", context) 

def list_view(request): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # add the dictionary during initialization 
    context["dataset"] = Article.objects.all() 
          
    return render(request, "liste.html", context) 

def intro (request):
    context = {}
    
    return render(request, "intro.html", context) 

def articles(request): 
    context ={} 
  
    form = ArticleForm(request.POST or None) 
    if form.is_valid(): 
        form.save() 
          
    context['form']= form 
    return render(request, "index.html", context) 