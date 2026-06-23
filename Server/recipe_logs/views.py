from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from recipes.models import Recipe

from .models import RecipeLog
from .serializers import (
    RecipeLogCreateSerializer,
    RecipeLogReadSerializer,
    RecipeLogUpdateSerializer,
)

RECIPE_NOT_FOUND_RESPONSE = {
    "code": "recipe_not_found",
    "detail": "Recipe does not exist.",
}


def recipe_exists_or_400(recipe_id):
    if Recipe.objects.filter(pk=recipe_id).exists():
        return None
    return Response(RECIPE_NOT_FOUND_RESPONSE, status=status.HTTP_400_BAD_REQUEST)


class RecipeLogListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, recipe_id):
        """
        Get all recipe logs for a recipe.
        """
        missing_recipe = recipe_exists_or_400(recipe_id)
        if missing_recipe is not None:
            return missing_recipe

        logs = RecipeLog.objects.filter(recipe_id=recipe_id)
        serializer = RecipeLogReadSerializer(logs, many=True)
        return Response(serializer.data)

    def post(self, request, recipe_id):
        """
        Create a new recipe log for a recipe.
        """
        missing_recipe = recipe_exists_or_400(recipe_id)
        if missing_recipe is not None:
            return missing_recipe

        serializer = RecipeLogCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        log = serializer.save(recipe_id=recipe_id)
        return Response(
            RecipeLogReadSerializer(log).data,
            status=status.HTTP_201_CREATED,
        )


class RecipeLogDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        """
        Update a recipe log.
        """
        log = get_object_or_404(RecipeLog, pk=pk)
        serializer = RecipeLogUpdateSerializer(
            log, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        log = serializer.save()
        return Response(RecipeLogReadSerializer(log).data)

    def put(self, request, pk):
        """
        Update a recipe log.
        """
        log = get_object_or_404(RecipeLog, pk=pk)
        serializer = RecipeLogUpdateSerializer(log, data=request.data)
        serializer.is_valid(raise_exception=True)
        log = serializer.save()
        return Response(RecipeLogReadSerializer(log).data)

    def delete(self, request, pk):
        """
        Delete a recipe log.
        """
        log = get_object_or_404(RecipeLog, pk=pk)
        log.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
