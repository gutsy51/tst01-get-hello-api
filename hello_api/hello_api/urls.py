from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


urlpatterns = [
    path('', lambda x: render(x, 'index.html'), name='index'),  # Home page.
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]



