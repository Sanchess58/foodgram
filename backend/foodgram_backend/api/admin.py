from django.contrib import admin
from .models import Recipes,  Tags, Ingridients

# class TagInline(admin.TabularInline):
#     model = Tags
#     extra = 0

@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Ingridients)
class IngridientsAdmin(admin.ModelAdmin):
    pass


class TagInline(admin.TabularInline):
    model = Recipes.tag.through
    extra = 0

class IngridientsInline(admin.TabularInline):
    model = Recipes.ingridients.through
    extra = 0


@admin.register(Recipes)
class ReceiptsAdmin(admin.ModelAdmin):
    inlines = [IngridientsInline, TagInline]
