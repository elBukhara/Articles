from django.shortcuts import render
from . models import Article


def articles_view(request):
    banger_article = Article.get_banger_article()
    
    articles_with_own_cover = Article.articles_with_own_cover_image()
    articles_with_own_cover = articles_with_own_cover.exclude(id=banger_article.id)
    
    articles_with_default_cover = Article.articles_with_default_cover_image()
    
    content = {
        'banger_article': banger_article,
        'articles_with_own_cover': articles_with_own_cover,
        'articles_with_default_cover': articles_with_default_cover
    }
    
    return render(request, 'blog/articles.html', content)

def article_view(request, slug):
    article = Article.objects.get(slug=slug)
    
    if article.cover_image == 'default/cover.jpg':
        cover_image = None
    else:
        cover_image = article.cover_image
    
    content = {
        'article': article,
        'cover_image': cover_image
    }
    
    return render(request, 'blog/article.html', content)
