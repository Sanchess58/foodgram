from api import exceptions, serializers
from .models import Favorites, ListShopping


def check_favorites_request_type(request, user, recipe):
    """Проверка типа запроса."""
    user_favorite_filter = user.favorites.filter(recipe=recipe)
    if request.method == 'POST':
        if user_favorite_filter.exists():
            raise exceptions.FavouriteException(
                {'errors': (f'Невозможно добавить {recipe.name}')},
            )
        Favorites.objects.create(user=user, recipe=recipe)
        serializer = serializers.ShortInfoRecipeSerializer(recipe)
        return serializer.data

    if request.method == 'DELETE':
        if user_favorite_filter.exists():
            user_favorite_filter.delete()
            return "delete"

        raise exceptions.FavouriteException(
            {'errors': f'В избранном нет рецепта \"{recipe.name}\"'}
        )


def check_list_shopping_request_type(request, user, recipe, pk):
    user_shopping_filter = user.buy.filter(recipe__id=pk)
    if request.method == 'POST':
        if user.buy.filter(recipe=recipe).exists():
            return exceptions.ListShopingException(
                {'errors': f'Повторно - \"{recipe.name}\" добавить нельзя,'
                    f'он уже есть в списке покупок'},
            )
        ListShopping.objects.create(user=user, recipe=recipe)
        serializer = serializers.ShortInfoRecipeSerializer(recipe)
        return serializer.data

    if request.method == 'DELETE':
        if user_shopping_filter.exists():
            user_shopping_filter.delete()
            return "delete"
        return exceptions.ListShopingException(
            {'errors': f'Нельзя удалить рецепт - \"{recipe.name}\", '
                f'которого нет в списке покупок '},
        )
