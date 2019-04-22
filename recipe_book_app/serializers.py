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
        fields = ('name',)


class RecipeListSerializer(ModelSerializer):
    item_id = IntegerField(source='item.id', read_only=True)
    name = CharField(source='item.name', read_only=True)

    class Meta:
        model = RecipeItem
        fields = ('id', 'item_id', 'is_result', 'name', 'qty')


class RecipeSerializer(ModelSerializer):
    items = RecipeListSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ('id', 'items', 'name')


class RecipeItemSerializer(ModelSerializer):
    item = ItemSerializer
    recipe = RecipeSerializer

    class Meta:
        model = RecipeItem
        fields = ('is_result', 'item', 'qty', 'recipe')






