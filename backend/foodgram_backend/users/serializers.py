from rest_framework.fields import IntegerField, SerializerMethodField
from djoser.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth import get_user_model
from .models import Follow
User = get_user_model()

class CustomUserSerializer(UserSerializer):
    is_subscribed = SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name'
        )

    # def get_is_subscribed(self, author):
    #     user = self.context.get('request').user
    #     if user.is_anonymous:
    #         return False
    #     return Follow.objects.filter(user=user, author=author).exists()