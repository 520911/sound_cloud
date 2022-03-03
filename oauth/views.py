from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import parsers, permissions

from .serializer import UserSerializer


class UserViewSet(ModelViewSet):
    parser_classes = (parsers.MultiPartParser,)
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user

    def get_object(self):
        return self.get_queryset()
