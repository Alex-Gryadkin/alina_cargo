from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('register/otpinput/', views.otp_input_view, name='otpinput'),
]