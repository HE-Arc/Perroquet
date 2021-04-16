from rest_framework import mixins, viewsets, permissions, generics
from rest_framework.authtoken.admin import User
from .serializers import RegisterSerializer, ChangePasswordSerializer


class RegisterViewSet(generics.CreateAPIView):
    """Create Only (POST)"""
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ChangePasswordSerializer