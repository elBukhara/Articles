from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from . models import Article, Hashtag

class ArticleForm(forms.ModelForm):
    hashtags = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter hashtags separated by commas'}))
    
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'cover_image', 'meta_description', 'keywords', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'minlength': 10, 'maxlength': 100, 'placeholder': 'Article Title'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 30, 'class': 'form-control'}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control'}),
            'meta_description': forms.Textarea(attrs={'cols': 80, 'rows': 3, 'class': 'form-control', 'minlength': 50, 'maxlength': 400, 'placeholder': 'Readers will be interested by this article with this description. 50-400 characters'}),
            'keywords': forms.Textarea(attrs={'cols': 80, 'rows': 3, 'class': 'form-control', 'placeholder': 'Keywords help searching engines find your article'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }
    
    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        # Pre-populate fields with current article values
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['title'].initial = instance.title
            self.fields['content'].initial = instance.content
            self.fields['category'].initial = instance.category_id
            self.fields['cover_image'].initial = instance.cover_image.url if instance.cover_image != 'default/cover.jpg' else 'default/cover.jpg'
            self.fields['meta_description'].initial = instance.meta_description
            self.fields['keywords'].initial = instance.keywords
            self.fields['hashtags'].initial = ', '.join(instance.hashtags.values_list('name', flat=True))


def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            form.save_m2m()  # Save the many-to-many data for the form
            hashtags = form.cleaned_data['hashtags']
            if hashtags:
                hashtag_list = [tag.strip() for tag in hashtags.split(',')]
                for tag in hashtag_list:
                    hashtag, created = Hashtag.objects.get_or_create(name=tag)
                    article.hashtags.add(hashtag)
            return redirect('blog:article', slug=article.slug)
    else:
        form = ArticleForm()

    return render(request, 'blog/create_article.html', {'form': form})

@login_required
def edit_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            form.save_m2m()  # Save the many-to-many data for the form
            hashtags = form.cleaned_data['hashtags']
            if hashtags:
                article.hashtags.clear()  # Clear existing hashtags
                hashtag_list = [tag.strip() for tag in hashtags.split(',')]
                for tag in hashtag_list:
                    hashtag, created = Hashtag.objects.get_or_create(name=tag)
                    article.hashtags.add(hashtag)
            return redirect('blog:article', slug=slug)
    else:
        form = ArticleForm(instance=article)

    return render(request, 'blog/edit_article.html', {'form': form, "article": article})

@login_required
def delete_article(request, slug):
    if Article.delete_article(slug=slug):
        return redirect('users:profile', user_id=request.user.id)

@login_required
def delete_cover_image(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.cover_image = 'default/cover.jpg'
    article.save()
    return HttpResponseRedirect(reverse('blog:edit_article', args=[article.slug]))
