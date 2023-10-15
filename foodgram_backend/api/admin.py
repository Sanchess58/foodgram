from django.contrib import admin
from .models import (
    Recipes,
    Tags,
    Ingredients,
    IngredientsInRecipe,
    Favorites,
    ListShopping
)


@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):
    pass


@admin.register(ListShopping)
class ListShoppingAdmin(admin.ModelAdmin):
    pass


@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Ingredients)
class IngridientsAdmin(admin.ModelAdmin):
    pass


class TagInline(admin.TabularInline):
    model = Recipes.tags.through
    extra = 0


class IngridientsInline(admin.TabularInline):
    model = Recipes.ingredients.through
    extra = 0


@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    inlines = [IngridientsInline, TagInline]


@admin.register(IngredientsInRecipe)
class IngredientsInRecipeAdmin(admin.ModelAdmin):
    pass
