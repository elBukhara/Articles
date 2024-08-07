from django.urls import path
from . import views
from . import forms
from . import search

app_name = 'blog' 

urlpatterns = [
    path('', views.articles_view, name='articles'),
    path('article/<slug:slug>', views.article_view, name='article'),
    path('category', views.category_list, name='category_list'),
    path('category/<slug:slug>', views.category_view, name='category'),
    
    path('create/', forms.create_article, name='create_article'),
    path('edit/<slug:slug>', forms.edit_article, name='edit_article'),
    path('delete/<slug:slug>', forms.delete_article, name='delete_article'),
    
    path('search', search.search_box, name='search'),
    path('search_suggestions/', search.search_suggestions, name='search_suggestions'),
]