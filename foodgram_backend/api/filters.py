import django_filters
from api import models as api_models
from rest_framework import filters


class IngredientsFilter(django_filters.FilterSet):
    """Фильтр для поиска ингредиента по его названию."""

    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = api_models.Ingredients
        fields = []


class RecipesTagsFilter(django_filters.FilterSet):
    """Фильтр для сортировки рецептов по тегам."""

    tags = django_filters.filters.ModelMultipleChoiceFilter(
        field_name='tags__slug',
        to_field_name='slug',
        queryset=api_models.Tags.objects.all(),
    )
    class Meta:
        model = api_models.Recipes
        fields = ('tags', 'author')


class FavoriteFilterBackend(filters.BaseFilterBackend):
    """Фильтр бекенд для избранного"""

    def filter_queryset(self, request, queryset, view):
        is_favorite = request.query_params.get('is_favorited')
        user = request.user

        if is_favorite is not None:
            queryset = queryset.filter(lover__user=user)

        return queryset


class ListShoppingFilterBackend(filters.BaseFilterBackend):
    """Фильтр бекенд для корзины"""

    def filter_queryset(self, request, queryset, view):
        is_in_shopping_cart = request.query_params.get('is_in_shopping_cart')
        user = request.user

        if is_in_shopping_cart is not None:
            queryset = queryset.filter(buyer__user=user)

        return queryset