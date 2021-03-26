# Create your views here.

from rest_framework import viewsets, mixins, generics, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter

from .models import User, Message
from .serializers import MessageSerializer, PublicUserProfileSerializer, UserSerializer, CreateMessageSerializer


class HelloView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        content = {
            'message': 'Hello, World!'
            }
        return Response(content)

class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = PublicUserProfileSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = UserSerializer(data=request.data,context={'request': request})
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = PublicUserProfileSerializer(instance=instance,context={'request': request})
    #     return Response(serializer.data)
    #
    # def list(self, request):
    #     instances = User.objects.all()
    #     serializer = PublicUserProfileSerializer(instances, many=True, context={'request': request})
    #     return Response(serializer.data)
    #
    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = PublicUserProfileSerializer(instance=instance,data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
    #
    # def get_serializer_class(self):
    #     if self.action == 'list' \
    #             or self.action == 'retrieve'\
    #             or self.action == 'update':
    #         return PublicUserProfileSerializer
    #     if self.action == 'create':
    #         return UserSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 10

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = StandardResultsSetPagination
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = CreateMessageSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=False,methods=['get'],url_name="discover")
    def discover(self, request):
        discover_msg = Message.objects.order_by('date').reverse().all()

        page = self.paginate_queryset(discover_msg)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(discover_msg, many=True)
        return Response(serializer.data)

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.content = "blabla"
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)
    #
    # def list(self, request):
    #     instances = Message.objects.all()
    #     serializer = MessageSerializer(instances,many=True, context={'request': request})
    #     return Response(serializer.data)


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