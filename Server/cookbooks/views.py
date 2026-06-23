from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Cookbook, CookbookRecipe
from .serializers import (
    CookbookRecipeReadSerializer,
    CookbookRecipeSerializer,
    CookbookSerializer,
)


class CookbookViewSet(ModelViewSet):
    serializer_class = CookbookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cookbook.objects.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


class CookbookRecipeListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get_cookbook(self, user_id, cookbook_id):
        return get_object_or_404(Cookbook, pk=cookbook_id, user_id=user_id)

    def get(self, request, cookbook_id):
        self.get_cookbook(request.user.id, cookbook_id)
        links = CookbookRecipe.objects.filter(cookbook_id=cookbook_id)
        serializer = CookbookRecipeReadSerializer(links, many=True)
        return Response(serializer.data)

    def post(self, request, cookbook_id):
        self.get_cookbook(request.user.id, cookbook_id)
        serializer = CookbookRecipeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        link, created = CookbookRecipe.objects.get_or_create(
            cookbook_id=cookbook_id,
            recipe_id=serializer.validated_data["recipe_id"],
        )
        if not created:
            return Response(
                {"detail": "Recipe is already in this cookbook."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            CookbookRecipeReadSerializer(link).data,
            status=status.HTTP_201_CREATED,
        )


class CookbookRecipeDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, cookbook_id, recipe_id):
        get_object_or_404(Cookbook, pk=cookbook_id, user_id=request.user.id)
        link = get_object_or_404(
            CookbookRecipe,
            cookbook_id=cookbook_id,
            recipe_id=recipe_id,
        )
        link.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
