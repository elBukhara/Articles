from django import forms
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe

from . models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'tags', 'cover_image', 'meta_description', 'keywords']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 30}),
            'meta_description': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
            'keywords': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
        }

    def render(self, *args, **kwargs):
        rendered_form = super().render(*args, **kwargs)
        return mark_safe(rendered_form.replace('<textarea', '<textarea class="form-control"'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field_obj in self.fields.items():
            if isinstance(field_obj.widget, forms.TextInput):
                field_obj.widget.attrs['class'] = 'form-control'
            elif isinstance(field_obj.widget, forms.Select):
                field_obj.widget.attrs['class'] = 'form-select'


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