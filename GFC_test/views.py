from django.http import HttpResponse
from django.shortcuts import render, redirect
from GFC_test.models import Article


def articles(request):
    names_from_db = Article.objects.all()
    context_dict = {'names_from_context': names_from_db}
    return render(request, 'index.html', context_dict)