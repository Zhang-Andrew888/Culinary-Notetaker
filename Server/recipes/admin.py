from django.contrib import admin

from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("dish_name", "cuisine_area", "user", "created_at")
    list_filter = ("cuisine_area",)
    search_fields = ("dish_name", "cuisine_area")
