from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from recipe_book_app.models import Recipe, RecipeItem, Item
from recipe_book_app.serializers import (
    RecipeItemSerializer,
    RecipeSerializer,
    ItemSerializer,
)
# Create your views here.


class RecipeViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer