from django.urls import path
from . import views

app_name = 'packages'

urlpatterns = [
    path('', views.packages_list, name='list'),
    path('del',views.PackagesDelete.as_view(), name='del'),
    path('add',views.PackagesAdd.as_view(), name='add'),
    path('statuslist',views.StatusList.as_view(), name='statuslist'),
]