from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField

class User(AbstractUser):
    profile_picture = models.ImageField(upload_to="profile_pictures", blank=True, null=True, default="default/profile_photo.jpg")
    bio = RichTextField(blank=True, null=True)
    
    def __str__(self):
        return self.username