from django.urls import path

from .views import RecipeLogDetailView, RecipeLogListCreateView

urlpatterns = [
    path(
        "<int:recipe_id>/logs/",
        RecipeLogListCreateView.as_view(),
        name="recipe-log-list-create",
    ),
    path(
        "logs/<int:pk>/",
        RecipeLogDetailView.as_view(),
        name="recipe-log-detail",
    ),
]
