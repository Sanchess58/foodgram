from api import exceptions as api_exception
from api import models as api_models
from api import serializers as api_serializers


def check_favorites_request_type(request, user, recipe):
    """Проверка типа запроса."""
    if request.method == 'POST':
        if api_models.Favorites.objects.filter(
            user=user,
            recipe=recipe
        ).exists():
            raise api_exception.FavouriteException(
                {'errors': (f'Невозможно добавить {recipe.name}')},
            )
        api_models.Favorites.objects.create(user=user, recipe=recipe)
        serializer = api_serializers.ShortInfoRecipeSerializer(recipe)
        return serializer.data

    if request.method == 'DELETE':
        if api_models.Favorites.objects.filter(
            user=user,
            recipe=recipe
        ).exists():
            api_models.Favorites.objects.filter(
                user=user,
                recipe=recipe
            ).delete()
            return "delete"

        raise api_exception.FavouriteException(
            {'errors': f'В избранном нет рецепта \"{recipe.name}\"'}
        )


def check_list_shopping_request_type(request, user, recipe, pk):
    if request.method == 'POST':
        if api_models.ListShopping.objects.filter(
            user=user,
            recipe=recipe
        ).exists():
            return api_exception.ListShopingException(
                {'errors': f'Повторно - \"{recipe.name}\" добавить нельзя,'
                    f'он уже есть в списке покупок'},
            )
        api_models.ListShopping.objects.create(user=user, recipe=recipe)
        serializer = api_serializers.ShortInfoRecipeSerializer(recipe)
        return serializer.data

    if request.method == 'DELETE':
        if api_models.ListShopping.objects.filter(
            user=user,
            recipe__id=pk
        ).exists():
            api_models.ListShopping.objects.filter(
                user=user,
                recipe__id=pk
            ).delete()
            return "delete"
        return api_exception.ListShopingException(
            {'errors': f'Нельзя удалить рецепт - \"{recipe.name}\", '
                f'которого нет в списке покупок '},
        )
