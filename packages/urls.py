from django.urls import path, include
from . import views

app_name = 'packages'
urlpatterns = [
    path('', views.packages_list, name='list'),
    path('del',views.PackagesDelete.as_view(), name='del'),
    path('add',views.PackagesAdd.as_view(), name='add')
]