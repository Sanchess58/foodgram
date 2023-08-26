from django.urls import path
from .views import CustomUserViewSet


urlpatterns = [
    path('users/', CustomUserViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('users/me/', CustomUserViewSet.as_view({'get': 'me'})),
]