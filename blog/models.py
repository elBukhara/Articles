import random

from django.db import models
from users.models import User
from django.template.defaultfilters import slugify

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Article(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=False)
    content = RichTextUploadingField(blank=True, null=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    tags = models.ManyToManyField('Tag', blank=True)
    cover_image = models.ImageField(upload_to='cover_image', blank=True, null=True, default='default/cover.jpg')
    meta_description = models.TextField(blank=False, null=False, default='')
    keywords = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Check if slug needs to be auto-generated
        if not self.slug:
            original_slug = slugify(self.title)
            # Check for uniqueness
            if Article.objects.filter(slug=original_slug).exists():
                # Append a number to make it unique
                count = 1
                while Article.objects.filter(slug=f"{original_slug}-{count}").exists():
                    count += 1
                self.slug = f"{original_slug}-{count}"
            else:
                self.slug = original_slug
        super(Article, self).save(*args, **kwargs)
    
    @classmethod
    def articles_with_default_cover_image(cls):
        return cls.objects.filter(cover_image='default/cover.jpg')
    
    @classmethod
    def articles_with_own_cover_image(cls):
        return cls.objects.exclude(cover_image='default/cover.jpg')
    
    @classmethod
    def get_banger_article(cls):
        """
        Returns the first article that meets the following criteria:
        - Description length is exactly 100 characters.
        - Has its own cover image (not the default one).
        - Content text length is more than 100 characters.
        """
        try:
            articles = cls.objects.exclude(cover_image='default/cover.jpg')
            
            banger_articles = [article for article in articles if len(article.meta_description) > 100 and article.content and len(article.content.strip()) > 1000]
            
            # Return the first matching article, or None if no articles match
            return random.choice(banger_articles[:3]) if banger_articles else None
        except IndexError:
            return None

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
