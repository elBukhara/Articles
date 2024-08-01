from django import forms
from django.shortcuts import render, redirect, get_object_or_404

from . models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'cover_image', 'meta_description', 'keywords']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 30, 'class': 'form-control'}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control'}),
            'meta_description': forms.Textarea(attrs={'cols': 80, 'rows': 3, 'class': 'form-control'}),
            'keywords': forms.Textarea(attrs={'cols': 80, 'rows': 3, 'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        # Pre-populate fields with current article values
        instance = getattr(self, 'instance', None)
        if instance:
            self.fields['title'].initial = instance.title
            self.fields['content'].initial = instance.content
            self.fields['category'].initial = instance.category_id
            self.fields['cover_image'].initial = instance.cover_image.url
            self.fields['meta_description'].initial = instance.meta_description
            self.fields['keywords'].initial = instance.keywords


def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            article.category.set(form.cleaned_data['tags'])
            return redirect('blog:articles')
    else:
        form = ArticleForm()

    return render(request, 'blog/create_article.html', {'form': form})

def edit_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('blog:articles')  # Redirect to the list of articles or wherever appropriate
    else:
        form = ArticleForm(instance=article)

    return render(request, 'blog/edit_article.html', {'form': form})