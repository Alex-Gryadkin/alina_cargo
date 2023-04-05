from django.urls import path, include
from . import views

app_name = 'packages'
urlpatterns = [
    path('', views.packages_list, name='list'),
    path('del',views.AjaxHandlerView.as_view(), name='del')
]