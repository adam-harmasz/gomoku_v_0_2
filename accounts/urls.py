from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'


urlpatterns = [
    # login and registration endpoints
    path('register', views.RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(
         template_name='registration/login.html',
         redirect_authenticated_user=True),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(
             template_name='registration/logout.html'), name='logout'),
    # detail view
    path('profile/<slug:slug>/', views.UserProfileView.as_view(),
         name='profile-detail'),
]
