from .models import Receipts
from rest_framework import serializers


class ReceiptsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipts
        fields = ['author', 'title', 'image']
