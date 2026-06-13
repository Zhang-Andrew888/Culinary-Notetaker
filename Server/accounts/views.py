from django.contrib.auth import login, logout
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


from .serializers import (
    LoginSerializer,
    RegisterSerializer,
    UserReadSerializer,
    UserUpdateSerializer,
)

class RegisterView(APIView):
    """
    Create a new user.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserReadSerializer(user).data,
                "tokens": _tokens_for_user(user),
            },
            status=status.HTTP_201_CREATED,
        )

def _tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "access": str(refresh.access_token),
        "refresh": str(refresh),
    }

class LoginView(APIView):
    """
    Login a user.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        return Response({
            "user": UserReadSerializer(user).data,
            "tokens": _tokens_for_user(user),
        })


class LogoutView(APIView):
    """
    Logout a user.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProfileView(APIView):
    """
    Get or update the user profile.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserReadSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request):
        serializer = UserUpdateSerializer(
            request.user, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserReadSerializer(user).data)