from django.urls import path

from api.views import APIHello


urlpatterns = [
    path('v1/', APIHello.as_view(), name='hello-api'),
]
