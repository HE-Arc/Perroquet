import os
import random
from datetime import datetime

from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers, fields
from rest_framework.validators import UniqueValidator

from .models import Message, Follow, Profile, Like
from django.contrib.auth.models import User
from django.db import models

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','bio','image')


class PublicUserProfileSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(required=False,allow_null=False)

    profile = ProfileSerializer(read_only=False)
    follow_count = serializers.SerializerMethodField(read_only=True)
    followers_count = serializers.SerializerMethodField(read_only=True)
    followed = serializers.SerializerMethodField(read_only=True)

    def get_follow_count(self,user):
        return user.follow.count()

    def get_followers_count(self,user):
        return user.followers.count()

    def get_followed(self,user):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            authuser = request.user
            follows = Follow.objects.filter(user__id=authuser.id).filter(following__id=user.id)
            if follows.count():
                return True
        return False

    class Meta:
        model = User
        fields = ('id','username','first_name', 'last_name', 'email','profile','followed','follow_count','followers_count','url'
        )

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def validate_username(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        if 'profile' in validated_data:
            profile_data = validated_data.pop('profile')
            profile = instance.profile

            profileSerializer = ProfileSerializer(data=profile_data)
            if (profileSerializer.is_valid()):
                profile.bio = profile_data.get('bio',profile.bio)
                profile.image = profile_data.get('image',profile.image)
                profile.save()

        return super(PublicUserProfileSerializer, self).update(instance,validated_data)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username','email','url')
    #
    # def create(self, validated_data):
    #     return User.objects.create_user(**validated_data)


#Inutile avec le perform_create dans la view
# class CreateMessageSerializer(serializers.ModelSerializer):
#     # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
#     user = serializers.PrimaryKeyRelatedField(read_only=True)
#
#     class Meta:
#         model = Message
#         fields = ['id','content','user','replyTo']

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    user = PublicUserProfileSerializer(read_only=True)
    like_count = serializers.SerializerMethodField(read_only=True)
    liked = serializers.SerializerMethodField(read_only=True)

    def get_liked(self,msg):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            likes = Like.objects.filter(message_id=msg.id).filter(user__id=user.id)
            if likes.count():
                return True
        return False

    def get_like_count(self,msg):
        return msg.like.count()

    class Meta:
        model = Message
        fields = ['id','date','like_count','liked','content','image','user','replyTo','url',]


class FollowSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    user = PublicUserProfileSerializer(read_only=True)
    following_id = serializers.IntegerField()
    following = PublicUserProfileSerializer(read_only=True)

    class Meta:
        model = Follow
        fields = ['id','user_id','user','following_id','following','date','url']

class LikeSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    user = PublicUserProfileSerializer(read_only=True)
    message_id = serializers.IntegerField()
    message = MessageSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ['id','user_id','user','message_id','message','date','url']