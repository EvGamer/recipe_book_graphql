from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField,
    CharField,
    IntegerField
)
from recipe_book_app.models import Item, Recipe, RecipeItem


class ItemSerializer(ModelSerializer):

    class Meta:
        model = Item
        fields = ('id', 'name',)


class RecipeListSerializer(ModelSerializer):
    item_id = IntegerField(source='item.id', read_only=True)
    item_name = CharField(source='item.name', read_only=True)

    class Meta:
        model = RecipeItem
        fields = ('id', 'item_id', 'item_name', 'is_result', 'qty')


class RecipeSerializer(ModelSerializer):
    items = RecipeListSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ('id', 'items', 'name')


class RecipeItemSerializer(ModelSerializer):
    item_id = PrimaryKeyRelatedField(source='item', required=True, queryset=Item.objects.all())
    item_name = CharField(source='item.name', read_only=True)

    recipe_id = PrimaryKeyRelatedField(source='recipe', required=True, queryset=Recipe.objects.all())
    recipe_name = CharField(source='recipe.name', read_only=True)

    class Meta:
        model = RecipeItem
        fields = ('id', 'item_id', 'item_name', 'is_result', 'qty', 'recipe_id', 'recipe_name')






