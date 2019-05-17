from django.shortcuts import render
from django.db.models import Q
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

    def get_queryset(self):
        params = self.request.query_params
        if {'in', 'out'}.intersection(params):
            return Recipe.objects.filter(
                items__item__name__contains=params.get('in', ''),
                items__is_result=False
            ).filter(
                items__item__name__contains=params.get('out', ''),
                items__is_result=True
            )

        return Recipe.objects.all()


class RecipeItemViewSet(ModelViewSet):
    queryset = RecipeItem.objects.all()
    serializer_class = RecipeItemSerializer


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

