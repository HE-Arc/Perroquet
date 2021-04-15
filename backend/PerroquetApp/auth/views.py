from rest_framework import mixins, viewsets, permissions, generics
from rest_framework.authtoken.admin import User
from .serializers import RegisterSerializer


class RegisterViewSet(generics.CreateAPIView):
    """Create Only (POST)"""
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer