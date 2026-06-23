from django.contrib import admin

from .models import Cookbook, CookbookRecipe


@admin.register(Cookbook)
class CookbookAdmin(admin.ModelAdmin):
    list_display = ("book_name", "user", "created_at")
    search_fields = ("book_name", "description")


@admin.register(CookbookRecipe)
class CookbookRecipeAdmin(admin.ModelAdmin):
    list_display = ("cookbook", "recipe")
