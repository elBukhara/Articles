from django.db import models
from users.models import User

from ckeditor.fields import RichTextField

class Article(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=False)
    content = RichTextField(blank=True, null=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    tags = models.ManyToManyField('Tag', blank=True)
    image = models.ImageField(upload_to='images/articles/%Y/%m/%d', blank=True)
    meta_description = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Automatically set the slug based on the title if it's not already set
        if not self.slug:
            self.slug = create_slug_from_title(self.title)
        super(Article, self).save(*args, **kwargs)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

def create_slug_from_title(title):
    """
    Helper function to create a URL slug from a title.
    """
    slug = title.replace(' ', '-').lower()
    return slug