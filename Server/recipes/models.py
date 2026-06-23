from django.conf import settings
from django.db import models


def default_list():
    return []


class Recipe(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="recipes",
    )
    dish_name = models.CharField(max_length=200)
    cuisine_area = models.CharField(max_length=100)
    steps = models.JSONField(default=default_list, blank=True)
    ingredients = models.JSONField(default=default_list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.dish_name
