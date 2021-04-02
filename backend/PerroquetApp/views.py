# Create your views here.

from rest_framework import viewsets, mixins, generics, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter

from .models import User, Message, Follow, Like
from .serializers import MessageSerializer, PublicUserProfileSerializer, UserSerializer, CreateMessageSerializer, \
    FollowSerializer, LikeSerializer


class IsOwner(permissions.BasePermission):
    message = "Not an owner"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.user


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

    @action(detail=True, methods=['get'], url_name="messages")
    def messages(self, request,pk):

        user_msg = Message.objects.order_by('date').filter(user__id=pk).reverse().all()

        page = self.paginate_queryset(user_msg)
        if page is not None:
            serializer = MessageSerializer(page, many=True,context={'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = MessageSerializer(user_msg, many=True,context={'request': request})
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_name="followers")
    def followers(self, request, pk):

        followers = Follow.objects.filter(following__id=pk).all()

        page = self.paginate_queryset(followers)
        if page is not None:
            serializer = FollowSerializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = FollowSerializer(followers, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_name="follows")
    def follows(self, request, pk):

        follows = Follow.objects.filter(user__id=pk).all()

        page = self.paginate_queryset(follows)
        if page is not None:
            serializer = FollowSerializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = FollowSerializer(follows, many=True, context={'request': request})
        return Response(serializer.data)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 10


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwner]
    http_method_names = ['get', 'post', 'delete']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#Pas besoin en fait
    # def create(self, request, *args, **kwargs):
    #     serializer = CreateMessageSerializer(data=request.data, context={'request': request})
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(user = request.user)
    #     return Response(serializer.data)

    @action(detail=False,methods=['get'],url_name="discover")
    def discover(self, request):
        discover_msg = Message.objects.order_by('date').reverse().all()

        page = self.paginate_queryset(discover_msg)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(discover_msg, many=True)
        return Response(serializer.data)

class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwner]
    http_method_names = ['get','post','delete']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwner]
    http_method_names = ['get','post','delete']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)