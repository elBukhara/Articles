from django.urls import path
from . import views
from . import authentication
from . import forms
app_name = 'users' 

urlpatterns = [
    path('profile/<int:user_id>/', views.profile_view, name='profile'),
    path('author/<int:author_id>/category/<slug:category_slug>/', views.users_category, name='users_category'),
    path('author/<int:author_id>/tag/<int:hashtag_id>/', views.users_hashtag, name='users_hashtag'),
    path('profile/edit_profile/', forms.edit_profile, name='edit_profile'),
    path('delete_profile_picture/<int:user_id>/', views.delete_profile_picture, name='delete_profile_picture'),
    
    path('login/', authentication.login_view, name='login'),
    path('register/', authentication.register, name='register'),
    path('logout/', authentication.logout_view, name='logout'),
]