from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blog.models import Article

# Create your views here.
@login_required
def profile_view(request):
    
    published_articles = Article.objects.filter(author=request.user, status='published')
    drafted_articles = Article.objects.filter(author=request.user, status='draft')
    
    context = {
        'published_articles': published_articles,
        'drafted_articles': drafted_articles
    }
    
    return render(request, 'users/profile.html', context)