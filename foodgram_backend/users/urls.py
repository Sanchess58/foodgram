from django.urls import path, include
from .views import CustomUserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('', CustomUserViewSet)


urlpatterns = [
    path('users/', include(router.urls)),
    path("auth/", include("djoser.urls.authtoken")),
]
