from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Ingridients(models.Model):
    name = models.CharField(verbose_name="Название ингридиента", null=False)
    measurement_unit = models.CharField(verbose_name="Единица измерения", max_length=5, null=False)

    class Meta:
        verbose_name = "Ингридиент"
        verbose_name_plural = "Ингридиенты"

    def __str__(self) -> str:
        return self.name


class Tags(models.Model):
    """Модель описывающая тег"""
    title = models.CharField(verbose_name="Название тега", null=False)
    hex_code = models.CharField(verbose_name="Код цвета", max_length=10, null=False)
    slug = models.SlugField(verbose_name="Слаг", null=False)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self) -> str:
        return self.title


class Receipts(models.Model):
    """Модель описывающая рецепты"""
    author = models.ForeignKey(User, related_name="author", verbose_name='Пользователь', on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Название", max_length=200, null=False)
    image = models.ImageField(upload_to="image/", null=False)
    ingridients = models.ManyToManyField(Ingridients, related_name="ingridients", verbose_name="Ингридиенты")
    text_description = models.TextField(verbose_name="Текстовое описание", null=False)
    cook_time = models.TimeField(verbose_name="Время приготовления", null=False)
    tag = models.ManyToManyField(Tags, verbose_name="Тег", related_name="tags")

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self) -> str:
        return f"{self.author} - {self.title}"