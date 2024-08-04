from django.urls import path
from . import views
from . import authentication
app_name = 'users' 

urlpatterns = [
    path('profile/<int:user_id>/', views.profile_view, name='profile'),
    path('author/<int:author_id>/category/<slug:category_slug>/', views.users_category, name='users_category'),
    
    path('login/', authentication.login_view, name='login'),
    path('register/', authentication.register, name='register'),
    path('logout/', authentication.logout_view, name='logout'),
]