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
    image = models.ImageField(upload_to='cover_image', blank=True)
    meta_description = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Check if slug needs to be auto-generated
        if not self.slug:
            original_slug = self.title.replace(' ', '-').lower()
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
    
    class Meta:
        ordering = ['-publish_date']


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
