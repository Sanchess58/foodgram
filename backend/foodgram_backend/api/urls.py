from django.urls import path, include
from .views import RecipesViewSet, TagViewSet, IngridientsViewSet
from rest_framework.routers import DefaultRouter
app_name = "api"

router = DefaultRouter()
router.register(r'recipes', RecipesViewSet, basename='recipes')
router.register(r'tags', TagViewSet, basename='tags')
router.register(r'ingredients', IngridientsViewSet, basename='ingredients')
urlpatterns = [
    path("", include(router.urls)),
]
