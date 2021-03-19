# Create your views here.

from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, Message
from .serializers import MessageSerializer, PublicUserProfileSerializer, UserSerializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {
            'message': 'Hello, World!'
            }
        return Response(content)

class UserViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):

    queryset = User.objects.all()
    # serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PublicUserProfileSerializer(instance=instance,context={'request': request})
        return Response(serializer.data)

    def list(self, request):
        instances = User.objects.all()
        serializer = PublicUserProfileSerializer(instances, many=True, context={'request': request})
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return PublicUserProfileSerializer
        if self.action == 'create':
            return UserSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.content = "blabla"
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def list(self, request):
        instances = Message.objects.all()
        serializer = MessageSerializer(instances,many=True, context={'request': request})
        return Response(serializer.data)


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