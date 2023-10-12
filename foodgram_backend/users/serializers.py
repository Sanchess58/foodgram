from djoser.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth import get_user_model
from .models import Follow
from rest_framework.fields import SerializerMethodField

User = get_user_model()


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name')


class CustomUserSerializer(UserSerializer):
    is_subscribed = SerializerMethodField(read_only=True)
    class Meta(UserSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'is_subscribed')
    
    def get_is_subscribed(self, author):
        request = self.context.get('request')
        if request.user.is_anonymous:
            return False
        return Follow.objects.filter(user=request.user, author=author).exists()
