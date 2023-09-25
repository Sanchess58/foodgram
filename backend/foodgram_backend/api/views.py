from rest_framework import viewsets, permissions, pagination
from .models import Recipes, Tags, Ingridients
from .serializers import ReceiptsViewSerializer, TagsSerializer, IngridientsSerializer
from rest_framework.decorators import action
from rest_framework import generics


class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size_query_param = 'limit'
    max_page_size = 6


class RecipesViewSet(viewsets.ModelViewSet):
    """CRUD для рецептов"""
    queryset = Recipes.objects.all()
    serializer_class = ReceiptsViewSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = CustomPageNumberPagination

    @action(detail=True, methods=['post'], permission_classes=permissions.IsAuthenticated)
    def perform_create(self, serializer):
        """Создание рецепта."""
        serializer.save(author=self.request.user)


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    """Просмотр тегов"""
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    pagination_class = CustomPageNumberPagination



class IngridientsViewSet(viewsets.ReadOnlyModelViewSet):
    """Просмотр ингридиентов"""
    queryset = Ingridients.objects.all()
    serializer_class = IngridientsSerializer
    pagination_class = CustomPageNumberPagination
