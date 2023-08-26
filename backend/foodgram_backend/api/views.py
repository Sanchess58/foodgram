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

    def perform_create(self, serializer):
        """Создание поста."""
        serializer.save(author=self.request.user)