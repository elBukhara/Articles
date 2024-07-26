from django.shortcuts import render
from . models import Article


def articles_view(request):
    articles = Article.objects.all()
    
    return render(request, 'blog/articles.html', {'articles': articles})

# def article_view(request):
#     return render(request, 'blog/article.html')

def article_view(request, pk):
    article = Article.objects.get(id=pk)
    
    context = {
        'article': article
    }
    
    return render(request, 'blog/article.html', context)
