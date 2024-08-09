from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Article, Category, Hashtag

class ArticleAdmin(ModelAdmin):
    list_display = ['title', 'author', 'status', 'type', 'category', 'publish_date', 'cover_image']
    filter_horizontal = ("hashtags",)
    # filter_horizontal = ("category",)
    # fields = ['title', 'content', 'publish_date', 'status', 'category', 'cover_image', 'meta_description', 'keywords', 'author']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Hashtag)