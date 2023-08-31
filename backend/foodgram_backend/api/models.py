from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import UniqueConstraint
from django.core.validators import MaxValueValidator, MinValueValidator


User = get_user_model()


class Ingridients(models.Model):
    name = models.CharField(verbose_name="Название ингридиента", null=False)
    measurement_unit = models.CharField(verbose_name="Единица измерения", null=False)

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


class Recipes(models.Model):
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
    

class IngredientRecipe(models.Model):
    """Модель для связи ингредиентов и рецептов."""

    ingredient = models.ForeignKey(
        Ingridients,
        on_delete=models.CASCADE,
        verbose_name='Ингредиент'
    )
    recipe = models.ForeignKey(
        Recipes,
        on_delete=models.CASCADE,
        related_name='recipe_ingredients',
        verbose_name='Рецепт'
    )
    amount = models.PositiveIntegerField(
        validators=[MaxValueValidator(1000),
                    MinValueValidator(1)],
        blank=False,
        verbose_name='Количество'
    )

    class Meta:
        ordering = ('recipe', 'id',)
        verbose_name = 'Ингредиенты рецепта'
        verbose_name_plural = 'Ингредиенты рецептов'
        constraints = [UniqueConstraint(
            fields=('recipe', 'ingredient'),
            name='unique_recipe_ingredient',
            violation_error_message='Этот ингредиент уже есть в рецепте.'
        )
        ]


class BaseUserRecipeRelation(models.Model):
    """Базовый класс для моделей с отношением рецепт-пользователь."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipes,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
    )

    class Meta:
        abstract = True
        constraints = [UniqueConstraint(
            fields=('user', 'recipe'),
            name='unique_user_and_relation_recipe')]

    def __str__(self):
        return f'{self.user} и {self.recipe}'


class Favorite(BaseUserRecipeRelation):
    """Модель для добавления рецептов в избранное."""

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
        constraints = [UniqueConstraint(
            fields=('user', 'recipe'),
            name='unique_user_and_favorite_recipe')]


class BuyList(BaseUserRecipeRelation):
    """Модель для добавления в БД рецептов в корзину."""

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        constraints = [UniqueConstraint(
            fields=('user', 'recipe'),
            name='unique_user_and_buylist_recipe')]