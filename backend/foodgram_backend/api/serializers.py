from .models import Recipes, Tags, Ingridients
from rest_framework import serializers
from django.core.files.base import ContentFile
import base64
import binascii

class ReceiptsViewSerializer(serializers.ModelSerializer):
    """Сериализатор для модели рецептов."""
    class Meta:
        model = Recipes
        fields = [
            'author',
            'title',
            'image',
            'text_description',
            'cook_time',
            'ingridients',
            'tag'
        ]


class TagsSerializer(serializers.ModelSerializer):
    "Сериализатор для модели тегов."
    class Meta:
        model = Tags
        fields = ['title', 'hex_code', 'slug']


class IngridientsSerializer(serializers.ModelSerializer):
    """Сериализатор для модели ингридиентов."""
    class Meta:
        model = Ingridients
        fields = ['name', 'measurement_unit']

    
class Base64ImageField(serializers.ImageField):
    """Класс для работы с изображениями в формате base64."""

    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            try:
                image_type, image_data = data.split(';base64,')
                image_extension = image_type.split('/')[-1]
                decoded_image = base64.b64decode(image_data)
                file_name = f'image.{image_extension}'
                data = ContentFile(decoded_image, name=file_name)
            except (ValueError, TypeError, binascii.Error):
                raise serializers.ValidationError('Invalid base64 format')
        return super().to_internal_value(data)
