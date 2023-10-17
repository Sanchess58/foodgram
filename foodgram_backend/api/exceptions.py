from rest_framework import status
from rest_framework.exceptions import APIException


class FavouriteException(APIException):
    """Кастомная ошибка для избранных рецептов."""
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Ошибка с избранными'
    default_code = 'validation_error'


class ListShopingException(APIException):
    """Кастомная ошибка для корзины."""
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Ошибка с добавлением рецепта в список покупок'
    default_code = 'validation_error'
