"""GFC_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.intro, name='intro'),
    path('admin/', admin.site.urls),
    path('articles/', views.articles, name='articles'),
    path('liste/', views.list_view, name='list_view'),
    path('liste/',include('django.contrib.auth.urls')),
    path('<id>/', views.detail_view), 
    path('<id>/update/', views.update_view, name='edit_article'), 
    path('<id>/delete/', views.delete_view, name='delete_article'), 
    
]

