from datetime import datetime, timedelta, date

from django.db import models
from django.db.models import Count, Case, When, IntegerField, Sum, Q
from rest_framework import viewsets, mixins, generics, permissions, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter

from .models import User, Message, Follow, Like
from .serializers import MessageSerializer, PublicUserProfileSerializer, \
    FollowSerializer, LikeSerializer


LIKE_PONDERATION = Case(
                        When(like__date__gt=datetime.today() - timedelta(hours=1), then=50),
                        When(like__date__gt=datetime.today() - timedelta(hours=12), then=25),
                        When(like__date__gt=datetime.today() - timedelta(days=1), then=10),
                        When(like__date__gt=datetime.today() - timedelta(days=2), then=5),
                        When(like__date__gt=datetime.today() - timedelta(days=5), then=2),
                        default=1,
                        output_field=IntegerField()
                    )

def sortMessages(obj, sortBy):
    if sortBy == "/hot":
        # Tri selon le nombre de like. Un like récent a une pondération + élevée
        return obj.annotate(
            count=Sum(LIKE_PONDERATION)
        ).order_by('count','date').reverse()

    elif sortBy == "/top":
        # Tri selon le nombre de like
        return obj.annotate(count=Count('like')).order_by('count','date').reverse()

    else:
        # Tri du messages
        return obj.order_by('date').reverse().all()

class IsOwner(permissions.BasePermission):
    message = "Not an owner"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.user

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 25

class FollowResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 100

class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = PublicUserProfileSerializer

    @action(detail=False, methods=['get'], url_name="me",permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        serializer = PublicUserProfileSerializer(request.user,context={'request': request}, many=False)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_name="messages", url_path='messages(?P<sortBy>/[a-z]*)?')
    def messages(self, request,pk, sortBy=None):
        user_msg = sortMessages(Message.objects.filter(user__id=pk), sortBy)

        pagination = StandardResultsSetPagination()
        page = pagination.paginate_queryset(user_msg,request)
        if page is not None:
            serializer = MessageSerializer(page, many=True,context={'request': request})
            return pagination.get_paginated_response(serializer.data)

        serializer = MessageSerializer(user_msg, many=True,context={'request': request})
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_name="followers")
    def followers(self, request, pk):

        followers = Follow.objects.filter(following__id=pk).all()

        pagination = FollowResultsSetPagination()
        page = pagination.paginate_queryset(followers, request)
        if page is not None:
            serializer = FollowSerializer(page, many=True, context={'request': request})
            return pagination.get_paginated_response(serializer.data)

        serializer = FollowSerializer(followers, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_name="follows")
    def follows(self, request, pk):

        follows = Follow.objects.filter(user__id=pk).all()

        pagination = FollowResultsSetPagination()
        page = pagination.paginate_queryset(follows, request)
        if page is not None:
            serializer = FollowSerializer(page, many=True, context={'request': request})
            return pagination.get_paginated_response(serializer.data)

        serializer = FollowSerializer(follows, many=True, context={'request': request})
        return Response(serializer.data)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwner]
    http_method_names = ['get', 'post', 'delete']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['get'], url_name="comments",
            url_path='comments(?P<sortBy>/[a-z]*)?')
    def comments(self, request,pk,sortBy=None):
        print(pk)
        comments_msg = sortMessages(Message.objects.filter(replyTo__id=pk), sortBy)

        page = self.paginate_queryset(comments_msg)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(comments_msg, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_name="home",permission_classes=[permissions.IsAuthenticated],
            url_path='home(?P<sortBy>/[a-z]*)?')
    def home(self, request,sortBy=None):
        follows = Follow.objects.filter(user__id=request.user.id).values_list("following",flat=True)
        home_msg = sortMessages(Message.objects.filter(user__in=follows), sortBy)

        page = self.paginate_queryset(home_msg)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(home_msg, many=True)
        return Response(serializer.data)

    @action(detail=False,methods=['get'], url_name="discover",url_path='discover(?P<sortBy>/[a-z]*)?')
    def discover(self, request, sortBy=None):
        discover_msg = sortMessages(Message.objects, sortBy)

        page = self.paginate_queryset(discover_msg)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(discover_msg, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_name="friends", permission_classes=[permissions.IsAuthenticated],
            url_path='friends(?P<sortBy>/[a-z]*)?')
    def friends(self, request, sortBy=None):
        follows = Follow.objects.filter(user__id=request.user.id).values_list("following", flat=True)
        followers = Follow.objects.filter(following_id=request.user.id).values_list("user", flat=True)
        friends = [value for value in follows if value in followers]

        friend_msg = sortMessages(Message.objects.filter(user__in=friends), sortBy)

        page = self.paginate_queryset(friend_msg)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(friend_msg, many=True)
        return Response(serializer.data)

class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwner]
    http_method_names = ['get','post','delete']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['delete'],url_path='(?P<pk>\d+)')
    def unfollow(self, request, pk):
        follow = Follow.objects.filter(user__id=request.user.id,following_id=pk).first()

        if follow is not None:
            follow.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_404_NOT_FOUND)

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwner]
    http_method_names = ['get','post','delete']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['delete'], url_path='(?P<pk>\d+)')
    def unlike(self, request, pk):
        like = Like.objects.filter(user__id=request.user.id, message_id=pk).first()

        if like is not None:
            like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_404_NOT_FOUND)