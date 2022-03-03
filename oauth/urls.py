from django.contrib import admin
from django.urls import path, include
from .oauth_views import google_login, google_auth

app_name = 'oauth'

urlpatterns = [
    path('google/', google_auth),
    path('', google_login)
]
