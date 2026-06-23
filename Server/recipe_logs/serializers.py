from rest_framework import serializers

from .models import RecipeLog

class RecipeLogReadSerializer(serializers.ModelSerializer):
    recipe_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = RecipeLog
        fields = ["id", "recipe_id", "notes", "date", "created_at"]
        read_only_fields = fields


class RecipeLogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeLog
        fields = ["notes", "date"]


class RecipeLogUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeLog
        fields = ["notes", "date"]
