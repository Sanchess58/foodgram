from djoser.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth import get_user_model
from .models import Follow

User = get_user_model()


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name')


class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'is_subscribed')
