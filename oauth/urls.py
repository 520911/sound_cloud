from django.urls import path
from rest_framework.routers import DefaultRouter

from .oauth_views import google_login, google_auth
from .views import UserViewSet

app_name = 'oauth'

router = DefaultRouter()
router.register('me', UserViewSet, basename='users')

urlpatterns = [
    path('google/', google_auth),
    path('', google_login)
] + router.urls
