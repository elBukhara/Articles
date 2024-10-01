from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from blog.models import Article, Category, Hashtag
from .models import User


def get_author_data(request, author):
    """
    Retrieves data related to a specific author.
    Args:
        author (User): The author for whom to retrieve data.
    Returns:
        dict: A dictionary containing the following keys:
            - 'author' (User): The author object.
            - 'categories_with_article_count' (QuerySet): A queryset of categories with the count of articles in each category, ordered by article count in descending order.
            - 'articles_in_hashtags' (QuerySet): A queryset of hashtags associated with the articles of the author.
    """
    articles = Article.objects.filter(author=author)
    
    categories_with_article_count = articles.filter(author=author) \
        .values('category__name', 'category__slug') \
        .annotate(article_count=Count('id')) \
        .order_by('-article_count') \
        .exclude(category__name=None)
    
    articles_in_hashtags =  Hashtag.objects.filter(article__in=articles).values('id', 'name')
    followers_count = author.get_followers().count()
    following_count = author.get_following().count()
    
    is_following = request.user.is_following(author) if (request.user.is_authenticated and request.user != author) else False
    
    content = {
        'author': author,
        'categories_with_article_count': categories_with_article_count,
        'articles_in_hashtags': articles_in_hashtags,
        'followers_count': followers_count,
        'following_count': following_count,
        'articles_count': articles.filter(status='published').count(),
        'is_following': is_following
    }
    
    return content

def profile_view(request, user_id):
    """
    Renders the profile view for a given user ID with corresponding data.
    """
    author = get_object_or_404(User, id=user_id)
    content = get_author_data(request, author)
    
    published_articles = Article.objects.filter(author=author, status='published')
    if request.user == author:
        drafted_articles = Article.objects.filter(author=author, status='draft')
    else:
        drafted_articles = []
    
    content.update({ 'published_articles': published_articles, 'drafted_articles': drafted_articles })
    
    return render(request, 'users/profile.html', content)

def users_category(request, author_id, category_slug):
    """
    Retrieves articles by author and category and renders the corresponding template.
    For example: Articles by Author in Category "Food"
    """
    
    author = get_object_or_404(User, id=author_id)
    content = get_author_data(request, author)

    
    category = get_object_or_404(Category, slug=category_slug)    
    articles = Article.objects.filter(author=author, category=category)
    
        
    content.update({
        'category': category,
        'articles': articles,
    })
        
    return render(request, 'users/partials/category_chosen.html', content)

def users_hashtag(request, author_id, hashtag_id):
    """
    Retrieves articles by author and hashtag and renders the corresponding template.
    For example: Articles by Author in Hashtag "France 2024"
    """
    author = get_object_or_404(User, id=author_id)
    content = get_author_data(request, author)
    
    hashtag = get_object_or_404(Hashtag, id=hashtag_id)
    articles = Article.objects.filter(author=author, hashtags=hashtag)
    
    content.update({
        'hashtag': hashtag,
        'articles': articles,
    })
    
    return render(request, 'users/partials/hashtag_chosen.html', content)

@login_required
def delete_profile_picture(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.profile_picture = 'default/profile_photo.jpg'
    user.save()
    return HttpResponseRedirect(reverse('users:edit_profile'))

@login_required
def follow_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    request.user.follow(user)
    return redirect('users:profile', user_id=user_id)

@login_required
def unfollow_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    request.user.unfollow(user)
    return redirect('users:profile', user_id=user_id)