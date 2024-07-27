from django.shortcuts import render
from . models import Article


def articles_view(request):
    banger_article = Article.objects.first()
    articles = Article.objects.exclude(id=banger_article.id)
    
    content = {
        'articles': articles,
        'banger_article': banger_article
    }
    
    # article_with_cover = Article.articles_with_default_cover_image()
    # article_without_cover = Article.articles_with_own_cover_image()
    
    return render(request, 'blog/articles.html', content)

def article_view(request, slug):
    article = Article.objects.get(slug=slug)
    
    content = {
        'article': article
    }
    
    return render(request, 'blog/article.html', content)
