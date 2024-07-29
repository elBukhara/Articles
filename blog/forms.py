from django import forms
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe

from . models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'tags', 'cover_image', 'meta_description', 'keywords']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 30, 'class': 'form-control'}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control'}),
            'meta_description': forms.Textarea(attrs={'cols': 80, 'rows': 3, 'class': 'form-control'}),
            'keywords': forms.Textarea(attrs={'cols': 80, 'rows': 3, 'class': 'form-control'}),
        }



def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('blog:articles')
    else:
        form = ArticleForm()

    return render(request, 'blog/create_article.html', {'form': form})