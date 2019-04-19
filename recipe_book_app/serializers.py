from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField
)
from recipe_book_app.models import Item, Recipe, RecipeItem


class RecipeSerializer(ModelSerializer):
    items = PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Recipe


class ItemSerializer(ModelSerializer):

    class Meta:
        model = Item


class RecipeItemSerializer(ModelSerializer):
    item = ItemSerializer

    class Meta:
        model = RecipeItem
