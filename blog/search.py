from django.http import JsonResponse
from django.db.models import Q

from django.shortcuts import render
from . models import Article
from . views import article_view


def search_box(request):
    query = request.GET.get('q')
    
    if query:
        if Article.objects.filter(title=query).exists():
            article = Article.objects.get(title=query)
            return article_view(request, article.slug)
        
        articles_found_in_title = Article.objects.filter(title__contains=query)
        articles_found_in_content = Article.objects.filter(
            Q(content__contains=query) |
            Q(meta_description__contains=query)
        )
        articles_found_in_content = list(set(articles_found_in_content) - set(articles_found_in_title))    
    else:
        articles_found_in_title = Article.objects.none()
        articles_found_in_content = Article.objects.none()
    
    content = {
        'articles_found_in_title': articles_found_in_title,
        'articles_found_in_content': articles_found_in_content,
        'query': query
    }
        
    return render(request, 'blog/results.html', content)

def search_suggestions(request):
    query = request.GET.get('q')
    if query:
        list1 = Article.objects.filter(title__contains=query)
        list2 = Article.objects.filter(meta_description__contains=query)
        results = list(set(list1) | set(list2))[:5]
        
        suggestions = [{'title': result.title} for result in results]
    else:
        suggestions = []
    return JsonResponse(suggestions, safe=False)