from django.urls import path, include
from .views import RecipesViewSet, TagsViewSet, IngredientsViewSet
from rest_framework.routers import DefaultRouter
app_name = "api"

router = DefaultRouter()
router.register(r'recipes', RecipesViewSet, basename='recipes')
router.register(r'tags', TagsViewSet, basename='tags')
router.register(r'ingredients', IngredientsViewSet, basename='ingredients')
urlpatterns = [
    path("", include(router.urls)),
]
