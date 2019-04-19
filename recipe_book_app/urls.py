from rest_framework.routers import DefaultRouter

from recipe_book_app.views import RecipeViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet, basename='recipe')

recipe_book_urls = router.urls