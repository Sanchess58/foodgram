from rest_framework import viewsets, permissions, pagination
from .models import Recipes
from .serializers import ReceiptsViewSerializer
from rest_framework.decorators import action


class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size_query_param = 'limit'
    max_page_size = 6

class ReceiptViewSet(viewsets.ModelViewSet):
    """CRUD для рецептов"""
    queryset = Recipes.objects.all()
    serializer_class = ReceiptsViewSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = pagination.LimitOffsetPagination

    @action(detail=True, methods=['post'], permission_classes=permissions.IsAuthenticated)
    def perform_create(self, serializer):
        """Создание рецепта."""
        serializer.save(author=self.request.user)