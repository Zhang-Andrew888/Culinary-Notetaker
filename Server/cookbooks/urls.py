from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    CookbookRecipeDetailView,
    CookbookRecipeListCreateView,
    CookbookViewSet,
)

router = DefaultRouter()
router.register("", CookbookViewSet, basename="cookbook")

urlpatterns = [
    path(
        "<int:cookbook_id>/recipes/",
        CookbookRecipeListCreateView.as_view(),
        name="cookbook-recipe-list-create",
    ),
    path(
        "<int:cookbook_id>/recipes/<int:recipe_id>/",
        CookbookRecipeDetailView.as_view(),
        name="cookbook-recipe-detail",
    ),
    *router.urls,
]
