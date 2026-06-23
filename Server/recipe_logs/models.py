from django.db import models

from recipes.models import Recipe


class RecipeLog(models.Model):
    """
    Notes about a recipe on a particular date. One recipe can have many logs.
    """
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="logs",
    )
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField()

    def __str__(self):
        return f"Log for {self.recipe.dish_name} on {self.date}"
