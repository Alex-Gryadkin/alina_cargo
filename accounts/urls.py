from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('password_reset/', views.password_reset_phone, name='password_reset'),
    path('password_reset/otp/', views.password_reset_otp, name='password_reset_otp'),
    path('password_reset/otp/new_password', views.new_password, name='new_password'),
    path('change_password/', views.change_password, name='change_password'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
]