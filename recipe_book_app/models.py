from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class RecipeItem(models.Model):
    is_result = models.BooleanField(default=False)
    qty = models.IntegerField(null=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.item.name
