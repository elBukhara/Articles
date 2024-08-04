from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from blog.models import Article, Category
from .models import User

# TODO: get articles from Author by Hashtag

def get_author_data(author):
    """
    Retrieves the categories with their respective article counts for a given author.
    Args:
        author (User): The author object for whom to retrieve the categories.
    Returns:
        QuerySet: A queryset containing the categories with their article counts.
            Each category is represented as a dictionary with the following keys:
            - 'category__name' (str): The name of the category.
            - 'category__slug' (str): The slug of the category.
            - 'article_count' (int): The number of articles in the category.
    Note:
        The queryset is ordered in descending order of article count.
        Categories with a null name are excluded from the result.
    """
    categories_with_article_count = Article.objects.filter(author=author) \
        .values('category__name', 'category__slug') \
        .annotate(article_count=Count('id')) \
        .order_by('-article_count')
    categories_with_article_count = categories_with_article_count.exclude(category__name=None)
    
    content = {
        'author': author,
        'categories_with_article_count': categories_with_article_count
    }
    
    return content

def profile_view(request, user_id):
    """
    Renders the profile view for a given user ID with corresponding data.
    """
    author = get_object_or_404(User, id=user_id)
    content = get_author_data(author)
    
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
    content = get_author_data(author)
    
    category = get_object_or_404(Category, slug=category_slug)    
    articles = Article.objects.filter(author=author, category=category)
    
        
    content.update({
        'category': category,
        'articles': articles,
    })
        
    return render(request, 'users/category_chosen.html', content)
