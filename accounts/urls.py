from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('password_reset/', views.password_reset_view, name='password_reset')
]