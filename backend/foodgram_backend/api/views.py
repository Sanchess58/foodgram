from django.shortcuts import render
from rest_framework import viewsets, permissions, pagination
from .models import Receipts
from .serializers import ReceiptsViewSerializer

class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size_query_param = 'limit'
    max_page_size = 6

class ReceiptViewSet(viewsets.ModelViewSet):
    """CRUD для рецептов"""
    queryset = Receipts.objects.all()
    serializer_class = ReceiptsViewSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = pagination.LimitOffsetPagination

    @permission_classes(permissions.IsAuthenticated) # type: ignore
    def create(self, request, *args, **kwargs):
        pass
    
    @permission_classes(permissions.IsAuthenticated) # type: ignore
    def retrieve(self, request, *args, **kwargs):
        pass