from rest_framework import serializers

from .models import Cookbook, CookbookRecipe


class CookbookSerializer(serializers.ModelSerializer):
    recipe_ids = serializers.SerializerMethodField()

    class Meta:
        model = Cookbook
        fields = [
            "id",
            "book_name",
            "description",
            "recipe_ids",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "recipe_ids", "created_at", "updated_at"]

    def get_recipe_ids(self, obj):
        return list(
            CookbookRecipe.objects.filter(cookbook_id=obj.id).values_list(
                "recipe_id", flat=True
            )
        )


class CookbookRecipeSerializer(serializers.Serializer):
    recipe_id = serializers.IntegerField()


class CookbookRecipeReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CookbookRecipe
        fields = ["recipe_id"]
        read_only_fields = ["recipe_id"]
