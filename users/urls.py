from django.urls import path
from . import views
from . import authentication
app_name = 'users' 

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    
    path('login/', authentication.login_view, name='login'),
    path('register/', authentication.register, name='register'),
    path('logout/', authentication.logout_view, name='logout'),
]