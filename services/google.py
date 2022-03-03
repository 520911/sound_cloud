from rest_framework.exceptions import AuthenticationFailed

from oauth.serializer import GoogleAuth
from google.oauth2 import id_token
from google.auth.transport import requests
from oauth.models import AuthUser
from services.base_auth import create_token
from django.conf import settings


def check_google_auth(google_user: GoogleAuth) -> dict:
    try:
        id_token.verify_oauth2_token(google_user['token'], requests.Request(), settings.GOOGLE_CLIENT_ID)
    except ValueError:
        raise AuthenticationFailed(code=403, detail='Bad token Google')

    user, _ = AuthUser.objects.get_or_create(email=google_user['email'])
    return create_token(user.id)
