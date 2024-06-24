from django import forms
from django.shortcuts import render, redirect
from . views import articles_view

from . models import Article, User

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'tags', 'image', 'meta_description', 'keywords']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 30}),
            'meta_description': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
            'keywords': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
        }


def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            articles_view(request)
    else:
        form = ArticleForm()

    return render(request, 'blog/create_article.html', {'form': form})