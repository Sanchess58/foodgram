from django.contrib import admin
from .models import Receipts, Tags, Ingridients

# class TagInline(admin.TabularInline):
#     model = Tags
#     extra = 0

@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Ingridients)
class IngridientsAdmin(admin.ModelAdmin):
    pass


class IngridientsInline(admin.TabularInline):
    model = Receipts.ingridients.through
    extra = 0


@admin.register(Receipts)
class ReceiptsAdmin(admin.ModelAdmin):
    inlines = [IngridientsInline]
