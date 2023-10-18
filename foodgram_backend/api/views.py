from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api import utils
from .filters import (FavoriteFilterBackend, IngredientsFilter,
                      ListShoppingFilterBackend, RecipesTagsFilter)
from .models import Ingredients, IngredientsInRecipe, Recipes, Tags
from .serializers import (IngredientsSerializer, RecipeCreateUpdateSerializer,
                          RecipesViewSerializer, TagsSerializer)


class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size_query_param = 'limit'
    max_page_size = 6


class RecipesViewSet(viewsets.ModelViewSet):
    """CRUD для рецептов"""
    queryset = Recipes.objects.all()
    serializer_class = RecipesViewSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = CustomPageNumberPagination
    filter_backends = [
        DjangoFilterBackend,
        FavoriteFilterBackend,
        ListShoppingFilterBackend
    ]
    filterset_class = RecipesTagsFilter

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return RecipesViewSerializer
        return RecipeCreateUpdateSerializer

    @action(
        detail=True,
        methods=['post'],
        permission_classes=[permissions.IsAuthenticated]
    )
    def perform_create(self, serializer):
        """Создание рецепта."""
        serializer.save(author=self.request.user)

    @action(
        detail=True,
        methods=['post', 'delete'],
        permission_classes=[permissions.IsAuthenticated],
        url_path='favorite',
        url_name='favorite',
    )
    def favorite(self, request, pk):
        """Метод для управления избранными подписками """
        user = request.user
        recipe = get_object_or_404(Recipes, id=pk)
        status_type = utils.check_favorites_request_type(request, user, recipe)
        if status_type == 'delete':
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status_type, status=status.HTTP_201_CREATED)

    @action(
        detail=True,
        methods=['post', 'delete'],
        permission_classes=[permissions.IsAuthenticated],
        url_path='shopping_cart',
        url_name='shopping_cart',
    )
    def shopping_cart(self, request, pk):
        """Метод для управления списком покупок"""

        user = request.user
        recipe = get_object_or_404(Recipes, id=pk)
        status_type = utils.check_list_shopping_request_type(
            request,
            user,
            recipe,
            pk
        )
        if status_type == 'delete':
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status_type, status=status.HTTP_201_CREATED)

    @action(
        detail=False,
        methods=['get'],
        permission_classes=[permissions.IsAuthenticated],
        url_path='download_shopping_cart',
        url_name='download_shopping_cart',
    )
    def download_shopping_cart(self, request):
        """Метод для загрузки ингредиентов"""

        ingredients = IngredientsInRecipe.objects.filter(
            recipe__buyer__user=request.user
        ).values(
            'ingredients__name',
            'ingredients__measurement_unit'
        ).annotate(sum=Sum('amount'))
        shopping_list = self.ingredients_to_txt(ingredients)
        return HttpResponse(shopping_list, content_type='text/plain')

    @staticmethod
    def ingredients_to_txt(ingredients):
        """Метод для объединения ингредиентов в список для скачивая"""

        shopping_list = ''
        for ingredient in ingredients:
            shopping_list += (
                f"{ingredient['ingredients__name']}  - "
                f"{ingredient['sum']}"
                f"({ingredient['ingredients__measurement_unit']})\n"
            )
        return shopping_list


class TagsViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет получения тегов"""
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    pagination_class = CustomPageNumberPagination


class IngredientsViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет получения ингредиентов"""
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = IngredientsFilter
