from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import User, Message
from .serializers import MessageSerializer, PublicUserProfileSerializer

from rest_framework import generics, permissions, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {
            'message': 'Hello, World!'
            }
        return Response(content)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = PublicUserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

# Utile pour retourner seulement certaines info si ce n\'est pas le proprio du profil
    # def get_serializer_context(self):
    #     if (user_owner):
    #         fields = {'blah', 'blah', 'blah'}
    #     else:
    #         fields = {'foo', 'bar'}
    #     return {'fields': fields, 'request': self.request}

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]



class UserViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """

    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

# class MessageList(generics.ListCreateAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = PublicUserProfileSerializer
#     permission_classes = [permissions.IsAuthenticated]

#
# class SubscriptionDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Subscription.objects.all()
#     serializer_class = SubscriptionSerializer