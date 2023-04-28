from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('accounts.urls')),
    path('', include('accounts.urls')),
    path('packages/', include('packages.urls')),
    path('p/', include('pages.urls')),

]
urlpatterns += staticfiles_urlpatterns()

