from django.urls import path
from . import views
from . import forms
app_name = 'blog' 

urlpatterns = [
    path('', views.articles_view, name='articles'),
    # path('article/', views.article_view, name='article'),
    path('article/<int:pk>', views.article_view, name='article'),
    
    
    path('article/create/', forms.create_article, name='create_article'),
]