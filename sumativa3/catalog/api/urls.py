from django.urls import path, include
from .api import api

urlpatterns = [
    path('v1/', api.urls)
]