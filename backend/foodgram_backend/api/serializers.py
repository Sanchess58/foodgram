from .models import Recipes
from rest_framework import serializers


class ReceiptsViewSerializer(serializers.ModelSerializer):
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
