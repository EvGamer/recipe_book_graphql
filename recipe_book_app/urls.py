from rest_framework.routers import DefaultRouter

import recipe_book_app.views as views

router = DefaultRouter()
router.register(r'recipes', views.RecipeViewSet, basename='recipe')
router.register(r'items', views.ItemViewSet, basename='item')
router.register(r'recipe-items', views.RecipeItemViewSet, basename='recipe-item')


recipe_book_urls = router.urls