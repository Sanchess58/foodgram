from rest_framework import viewsets, permissions, pagination
from django.contrib.auth import get_user_model
from djoser.views import UserViewSet
User = get_user_model()


class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    pagination_class = pagination.PageNumberPagination