from django.contrib import admin
from .models import Recipes,  Tags, Ingridients


@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Ingridients)
class IngridientsAdmin(admin.ModelAdmin):
    pass


class TagInline(admin.TabularInline):
    model = Recipes.tags.through
    extra = 0

class IngridientsInline(admin.TabularInline):
    model = Recipes.ingredients.through
    extra = 0


@admin.register(Recipes)
class ReceiptsAdmin(admin.ModelAdmin):
    inlines = [IngridientsInline, TagInline]
