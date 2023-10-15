from rest_framework.exceptions import APIException


class FavouriteException(APIException):
    """Кастомная ошибка для избранных рецептов."""
    status_code = 400
    default_detail = 'Ошибка с избранными'
    default_code = 'validation_error'


class ListShopingException(APIException):
    """Кастомная ошибка для корзины."""
    status_code = 400
    default_detail = 'Ошибка с добавлением рецепта в список покупок'
    default_code = 'validation_error'
