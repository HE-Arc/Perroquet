# Create your views here.

from rest_framework import viewsets, mixins, generics, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter

from .models import User, Message, Follow
from .serializers import MessageSerializer, PublicUserProfileSerializer, UserSerializer, CreateMessageSerializer, \
    FollowSerializer


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


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 10


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsOwner]

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

    def get_queryset(self):
        print(self.request.method)
        if self.request.method == 'POST':
            return self.queryset.filter(author=self.request.user)
        else:
            return self.queryset

class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsOwner]