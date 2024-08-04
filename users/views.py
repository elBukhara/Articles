from django.shortcuts import render
from blog.models import Article

# Create your views here.

def profile_view(request):
    
    published_articles = Article.objects.filter(author=request.user, status='published')
    drafted_articles = Article.objects.filter(author=request.user, status='draft')
    
    context = {
        'published_articles': published_articles,
        'drafted_articles': drafted_articles
    }
    
    return render(request, 'users/profile.html', context)