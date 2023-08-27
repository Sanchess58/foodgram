from .models import Recipes, Tags, Ingridients
from rest_framework import serializers


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
