from rest_framework import permissions, pagination
from django.contrib.auth import get_user_model
from djoser.views import UserViewSet
from djoser import views

User = get_user_model()


class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    pagination_class = pagination.PageNumberPagination
