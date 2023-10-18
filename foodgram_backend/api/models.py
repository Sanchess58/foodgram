from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()


class Ingredients(models.Model):
    name = models.CharField(verbose_name='Название ингредиента')
    measurement_unit = models.CharField(
        verbose_name='Единица измерения',
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name


class Tags(models.Model):
    """Модель описывающая тег"""
    name = models.CharField(verbose_name='Название тега')
    color = models.CharField(
        verbose_name='Код цвета',
        max_length=10,
    )
    slug = models.SlugField(verbose_name='Слаг')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name


class Recipes(models.Model):
    """Модель описывающая рецепты"""
    author = models.ForeignKey(
        User,
        related_name='author',
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
    )
    image = models.ImageField(upload_to='image/')
    ingredients = models.ManyToManyField(
        Ingredients,
        related_name='recipes',
        verbose_name='Ингредиенты'
    )
    text = models.TextField(
        verbose_name='Текстовое описание',
    )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления',
        validators=[
            MinValueValidator(settings.MIN_AMOUNT),
            MaxValueValidator(settings.MAX_AMOUNT)
        ]
    )
    tags = models.ManyToManyField(
        Tags,
        verbose_name='Теги',
        related_name='recipes'
    )
    is_favorited = models.BooleanField(
        verbose_name='В избранном ли',
        default=False
    )
    is_in_shopping_cart = models.BooleanField(
        verbose_name='Находится ли в корзине',
        default=False
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('cooking_time', 'name')

    def __str__(self) -> str:
        return f'{self.author} - {self.name}'


class IngredientsInRecipe(models.Model):
    """Модель связи ингредиентов и рецепта."""
    recipe = models.ForeignKey(
        Recipes,
        on_delete=models.CASCADE,
        related_name='ingredient_in_recipe',
        verbose_name='Рецепт'
    )
    ingredients = models.ForeignKey(
        Ingredients,
        on_delete=models.CASCADE,
        related_name='ingredient_in_recipe',
        verbose_name='Ингредиенты'
    )
    amount = models.PositiveSmallIntegerField(
        verbose_name='Количество',
        validators=[
            MinValueValidator(settings.MIN_AMOUNT),
            MaxValueValidator(settings.MAX_AMOUNT)
        ]
    )

    class Meta:
        verbose_name = 'Ингредиенты в рецепте'
        verbose_name_plural = 'Ингредиенты в рецептах'
        ordering = ('amount',)

    def __str__(self):
        return f'{self.ingredients} в {self.recipe}'


class TagRecipe(models.Model):
    """Модель связи тегов и рецепта."""

    tag = models.ForeignKey(
        Tags,
        on_delete=models.CASCADE,
        related_name='tags_in_recipe',
        verbose_name='Тег'
    )
    recipe = models.ForeignKey(
        Recipes,
        on_delete=models.CASCADE,
        related_name='tags_in_recipe',
        verbose_name='Рецепт'
    )

    class Meta:
        verbose_name = 'Теги в рецепте'
        verbose_name_plural = 'Теги в рецептах'
        ordering = ('id',)

    def __str__(self):
        return f'{self.tag} в {self.recipe}'


class ListShopping(models.Model):
    """Модель описывающая cписок покупок."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='buy',
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipes,
        on_delete=models.CASCADE,
        related_name='buyer',
        verbose_name='Рецепт'
    )

    class Meta:
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Списки покупок'
        ordering = ('id',)

    def __str__(self):
        return f'у {self.user} есть {self.recipe}'


class Favorites(models.Model):
    """Модель избранных рецептов."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipes,
        on_delete=models.CASCADE,
        related_name='lover',
        verbose_name='Рецепт'
    )

    class Meta:
        verbose_name = 'Избранный рецепт'
        verbose_name_plural = 'Избранные рецепты'
        ordering = ('id',)

        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_favorite'
            )
        ]

    def __str__(self):
        return f'{self.recipe} в избранных у {self.user}'
