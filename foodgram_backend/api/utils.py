from api import exceptions, serializers

from .models import Favorites, ListShopping


def check_favorites_request_type(request, user, recipe):
    """Проверка типа запроса."""
    if request.method == 'POST':
        if user.favorites.filter(recipe=recipe).exists():
            raise exceptions.FavouriteException(
                {'errors': (f'Невозможно добавить {recipe.name}')},
            )
        Favorites.objects.create(user=user, recipe=recipe)
        serializer = serializers.ShortInfoRecipeSerializer(recipe)
        return serializer.data

    if request.method == 'DELETE':
        if user.favorites.filter(recipe=recipe).exists():
            user.favorites.filter(recipe=recipe).delete()
            return "delete"

        raise exceptions.FavouriteException(
            {'errors': f'В избранном нет рецепта \"{recipe.name}\"'}
        )


def check_list_shopping_request_type(request, user, recipe, pk):
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
        if user.buy.filter(recipe__id=pk).exists():
            user.buy.filter(recipe__id=pk).delete()
            return "delete"
        return exceptions.ListShopingException(
            {'errors': f'Нельзя удалить рецепт - \"{recipe.name}\", '
                f'которого нет в списке покупок '},
        )
