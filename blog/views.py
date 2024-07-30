from django.shortcuts import render
from . models import Article
from django.core.paginator import Paginator

def articles_view(request):
    banger_article = Article.get_banger_article()
    
    articles_with_own_cover = Article.articles_with_own_cover_image()
    articles_with_own_cover = articles_with_own_cover.exclude(id=banger_article.id)
    
    p1 = Paginator(articles_with_own_cover, 2)
    page_own_cover = request.GET.get('page_own_cover')
    articles_with_own_cover = p1.get_page(page_own_cover)
    
    articles_with_default_cover = Article.articles_with_default_cover_image()
    
    p2 = Paginator(articles_with_default_cover, 3)
    page_default_cover = request.GET.get('page_default_cover')
    articles_with_default_cover = p2.get_page(page_default_cover)
    
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
