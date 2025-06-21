from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer
from django.contrib.auth.models import User

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

class UserOnlyView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({"message": f"Hello, {request.user.username}! You are a user"})

class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        if not request.user.is_staff:
            return Response({"message": "Admins only!"},status=403)
        return Response({"message": f"Hello Admin {request.user.username}!"})

