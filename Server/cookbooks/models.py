from django.conf import settings
from django.db import models

from recipes.models import Recipe


class Cookbook(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="cookbooks",
    )
    book_name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    recipes = models.ManyToManyField(
        Recipe,
        through="CookbookRecipe",
        related_name="cookbooks",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book_name


class CookbookRecipe(models.Model):
    cookbook = models.ForeignKey(
        Cookbook,
        on_delete=models.CASCADE,
        related_name="cookbook_recipes",
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="cookbook_recipes",
    )

    class Meta:
        db_table = "cookbook_recipes"
        unique_together = [("cookbook", "recipe")]

    def __str__(self):
        return f"{self.cookbook.book_name} - {self.recipe.dish_name}"
