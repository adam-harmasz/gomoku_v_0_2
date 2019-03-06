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

    # password reset views
    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    # detail view
    path('profile/<slug:slug>/', views.UserProfileView.as_view(),
         name='profile-detail'),

]
