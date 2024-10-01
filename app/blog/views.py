from django.shortcuts import render
from . models import Article, Category
from django.core.paginator import Paginator

def articles_view(request):
    banger_article = Article.get_banger_article()
    
    articles_with_own_cover = Article.articles_with_own_cover_image().filter(status='published')
    if banger_article:
        articles_with_own_cover = articles_with_own_cover.exclude(id=banger_article.id)
    articles_with_own_cover = articles_with_own_cover.exclude(type='carousel')
    
    articles_with_carousel = Article.objects.filter(type='carousel')[:3]
    
    p1 = Paginator(articles_with_own_cover, 2)
    page_own_cover = request.GET.get('page_own_cover')
    articles_with_own_cover = p1.get_page(page_own_cover)
    
    articles_with_default_cover = Article.articles_with_default_cover_image().filter(status='published')
    
    p2 = Paginator(articles_with_default_cover, 3)
    page_default_cover = request.GET.get('page_default_cover')
    articles_with_default_cover = p2.get_page(page_default_cover)
    
    categories = Category.get_random()
    first_half_categories = categories[:(len(categories)//2)]
    second_half_categories = categories[(len(categories)//2):]
    
    content = {
        'banger_article': banger_article,
        'articles_with_own_cover': articles_with_own_cover,
        'articles_with_default_cover': articles_with_default_cover,
        'first_half_categories': first_half_categories,
        'second_half_categories': second_half_categories,
        'articles_with_carousel': articles_with_carousel if len(articles_with_carousel) == 3 else None
    }
    
    return render(request, 'blog/articles.html', content)

def article_view(request, slug):
    article = Article.objects.get(slug=slug)
    
    if article.cover_image == 'default/cover.jpg':
        cover_image = None
    else:
        cover_image = article.cover_image
        
    hashtags = article.hashtags.all()
    categories = Category.get_random()
    first_half_categories = categories[:(len(categories)//2)]
    second_half_categories = categories[(len(categories)//2):]
    
    content = {
        'article': article,
        'hashtags': hashtags,
        'cover_image': cover_image,
        'first_half_categories': first_half_categories,
        'second_half_categories': second_half_categories
    }
    
    return render(request, 'blog/article.html', content)

def category_list(request):
    categories = Category.objects.all()
    random_article = Article.objects.order_by('?').first()
    content = {
        'categories': categories,
        'article': random_article
    }
    
    return render(request, 'blog/category_list.html', content)

def category_view(request, slug):
    category = Category.objects.get(slug=slug)
    articles_with_own_cover = Article.articles_with_own_cover_image().filter(category=category, status='published')
    articles_with_default_cover = Article.articles_with_default_cover_image().filter(category=category, status='published')
    random_article = Article.objects.order_by('?').first()
    
    categories = Category.get_random()
    first_half_categories = categories[:(len(categories)//2)]
    second_half_categories = categories[(len(categories)//2):]
    
    content = {
        'category': category,
        'articles_with_own_cover': articles_with_own_cover,
        'articles_with_default_cover': articles_with_default_cover,
        'article': random_article,
        'first_half_categories': first_half_categories,
        'second_half_categories': second_half_categories
    }
    
    return render(request, 'blog/category.html', content)