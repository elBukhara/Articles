from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

class Subscription(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f"{self.follower} follows {self.following}"

class User(AbstractUser):
    profile_picture = models.ImageField(upload_to="profile_pictures", blank=True, null=True, default="default/profile_photo.jpg")
    bio = RichTextField(blank=True, null=True)
    location = models.CharField(max_length=40, blank=True, null=True)
    
    def __str__(self):
        return self.username
    
    def follow(self, user):
        Subscription.objects.get_or_create(follower=self, following=user)

    def unfollow(self, user):
        Subscription.objects.filter(follower=self, following=user).delete()

    def is_following(self, user):
        return Subscription.objects.filter(follower=self, following=user).exists()

    def is_followed_by(self, user):
        return Subscription.objects.filter(following=self, follower=user).exists()
    
    def get_followers(self):
        return User.objects.filter(following__following=self)

    def get_following(self):
        return User.objects.filter(followers__follower=self)