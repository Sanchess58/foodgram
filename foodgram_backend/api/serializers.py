import base64

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework import serializers, status, validators

from users.serializers import CustomUserSerializer
from .models import Ingredients, IngredientsInRecipe, Recipes, Tags


class IngredientsInRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        models = IngredientsInRecipe
        fields = ('__all__',)


class TagsSerializer(serializers.ModelSerializer):
    """Сериализатор для модели тегов."""
    class Meta:
        model = Tags
        fields = ('id', 'name', 'color', 'slug')


class IngredientsSerializer(serializers.ModelSerializer):
    """Сериализатор для модели ингридиентов."""
    class Meta:
        model = Ingredients
        fields = ('id', 'name', 'measurement_unit')


class Base64ImageField(serializers.ImageField):
    """Класс для работы с изображениями в формате base64."""

    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='photo.' + ext)

        return super().to_internal_value(data)


class IngredientInRecipeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='ingredients.id')

    name = serializers.CharField(
        source='ingredients.name',
        read_only=True,
    )
    measurement_unit = serializers.CharField(
        source='ingredients.measurement_unit',
        read_only=True,
    )

    amount = serializers.IntegerField()

    class Meta:
        model = IngredientsInRecipe
        fields = (
            'id',
            'name',
            'measurement_unit',
            'amount',
        )


class RecipesViewSerializer(serializers.ModelSerializer):
    """Сериализатор для модели рецептов."""
    tags = TagsSerializer(many=True)
    ingredients = IngredientInRecipeSerializer(
        source='ingredient_in_recipe',
        many=True
    )
    image = Base64ImageField()
    author = CustomUserSerializer(required=False)
    is_favorited = serializers.SerializerMethodField(read_only=True)
    is_in_shopping_cart = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Recipes
        fields = (
            'id',
            'tags',
            'author',
            'ingredients',
            'is_favorited',
            'is_in_shopping_cart',
            'name',
            'image',
            'text',
            'cooking_time',
        )

    def get_is_favorited(self, obj):
        """Метод проверки на добавление в избранное."""
        request = self.context['request']
        if request is None or request.user.is_anonymous:
            return False
        return request.user.favorites.filter(recipe=obj).exists()

    def get_is_in_shopping_cart(self, obj):
        """Метод проверки на присутствие в корзине."""

        request = self.context['request']
        if request is None or request.user.is_anonymous:
            return False
        return request.user.buy.filter(recipe=obj).exists()


class CreateIngredientsInRecipeSerializer(serializers.ModelSerializer):
    """Сериализатор для ингредиентов в рецептах"""

    id = serializers.IntegerField()
    amount = serializers.IntegerField(
        validators=[
            MinValueValidator(settings.MIN_AMOUNT),
            MaxValueValidator(settings.MAX_AMOUNT)
        ]
    )

    class Meta:
        model = IngredientsInRecipe
        fields = ('id', 'amount')


class RecipeCreateUpdateSerializer(serializers.ModelSerializer):
    ingredients = CreateIngredientsInRecipeSerializer(many=True)
    tags = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Tags.objects.all()
    )
    image = Base64ImageField()
    author = CustomUserSerializer(required=False)
    cooking_time = serializers.IntegerField(
        validators=[
            MinValueValidator(settings.MIN_AMOUNT),
            MaxValueValidator(settings.MAX_AMOUNT)
        ]
    )

    class Meta:
        model = Recipes
        fields = ('id', 'tags', 'author', 'ingredients', 'is_favorited',
                  'is_in_shopping_cart', 'name', 'image', 'text',
                  'cooking_time')

    def create_ingredients(self, ingredients, recipe):
        """Метод создания ингредиента"""
        IngredientsInRecipe.objects.bulk_create(
            [IngredientsInRecipe(
                ingredients=Ingredients.objects.get(
                    id=ingredient['id']
                ),
                recipe=recipe,
                amount=ingredient['amount']
            ) for ingredient in ingredients]
        )

    def create_tags(self, tags, recipe):
        """Метод добавления тега"""
        recipe.tags.set(tags)

    def create(self, validated_data):
        ingredients = validated_data.pop('ingredients')
        tags = validated_data.pop('tags')
        recipe = Recipes.objects.create(**validated_data)
        self.create_ingredients(ingredients, recipe)
        self.create_tags(tags, recipe)
        return recipe

    def update(self, instance, validated_data):

        self.create_ingredients(validated_data.pop('ingredients'), instance)
        self.create_tags(validated_data.pop('tags'), instance)

        return super().update(instance, validated_data)


class ShortInfoRecipeSerializer(serializers.ModelSerializer):
    """Сериализатор для добавления в избранное."""
    image = Base64ImageField()

    class Meta:
        model = Recipes
        fields = ('id', 'name', 'image', 'cooking_time')


class FollowSerializer(CustomUserSerializer):
    recipes_count = serializers.SerializerMethodField()
    recipes = serializers.SerializerMethodField()

    class Meta(CustomUserSerializer.Meta):
        fields = (
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'is_subscribed',
            'recipes_count',
            'recipes'
        )
        read_only_fields = ('email', 'username')

    def validate(self, data):
        author = self.instance
        user = self.context['request'].user
        if user.follower.filter(author=author).exists():
            raise validators.ValidationError(
                detail='Вы уже подписаны на этого пользователя!',
                code=status.HTTP_400_BAD_REQUEST
            )
        if user == author:
            raise validators.ValidationError(
                detail='Вы не можете подписаться на самого себя!',
                code=status.HTTP_400_BAD_REQUEST
            )
        return data

    def get_recipes_count(self, obj):
        return obj.author.count()

    def get_recipes(self, obj):
        request = self.context['request']
        limit = request.GET.get('recipes_limit')
        recipes = obj.author.all()
        if limit:
            recipes = recipes[:int(limit)]
        serializer = ShortInfoRecipeSerializer(
            recipes,
            many=True,
            read_only=True
        )
        return serializer.data
