from rest_framework.routers import DefaultRouter

import recipe_book_app.views as views

router = DefaultRouter()
router.register(r'recipes', views.RecipeViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'recipe-items', views.RecipeItemViewSet)


recipe_book_urls = router.urls