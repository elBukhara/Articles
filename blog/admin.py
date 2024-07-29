from django.contrib import admin
from django.db import models
from django.forms import DateTimeInput
from django.contrib.admin import ModelAdmin
from .models import Article, Tag

class ArticleAdmin(ModelAdmin):
    list_display = ['title', 'status', 'publish_date', 'cover_image']
    filter_horizontal = ("tags",)
    # fields = ['title', 'content', 'publish_date', 'status', 'tags', 'cover_image', 'meta_description', 'keywords', 'author']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
