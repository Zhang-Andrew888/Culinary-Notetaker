from rest_framework import serializers

from .models import Recipe


class IngredientSerializer(serializers.Serializer):
    name = serializers.CharField()
    amount = serializers.CharField()


class RecipeSerializer(serializers.ModelSerializer):
    steps = serializers.ListField(child=serializers.CharField(), allow_empty=True)
    ingredients = IngredientSerializer(many=True, allow_empty=True)

    class Meta:
        model = Recipe
        fields = [
            "id",
            "dish_name",
            "cuisine_area",
            "steps",
            "ingredients",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
