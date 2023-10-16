from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CustomUserViewSet

router = DefaultRouter()

router.register('', CustomUserViewSet)


urlpatterns = [
    path('users/', include(router.urls)),
    path("auth/", include("djoser.urls.authtoken")),
]
