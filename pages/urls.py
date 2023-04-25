from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('nav/',views.NavRender.as_view(), name='nav'),
    path("<slug:slug>/", views.page_view, name='page'),
]