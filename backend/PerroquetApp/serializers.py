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
        fields = ('id','bio','image'
        )


class PublicUserProfileSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer(read_only=False)
    # follow = serializers.StringRelatedField(many=True)
    follow_count = serializers.SerializerMethodField(read_only=True)
    followers_count = serializers.SerializerMethodField(read_only=True)

    def get_follow_count(self,user):
        return user.follow.count()

    def get_followers_count(self,user):
        return user.followers.count()

    class Meta:
        model = User
        fields = ('id','username','first_name', 'last_name', 'profile','follow_count','followers_count','url'
        )

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        print(profile_data)
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
class CreateMessageSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Message
        fields = ['id','content','user','replyTo']

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    user = PublicUserProfileSerializer(read_only=True)
    # user_id = serializers.PrimaryKeyRelatedField(
    #     queryset=User.objects.all(), source='user', write_only=True)

    class Meta:
        model = Message
        fields = ['id','date','content','image','user','replyTo','url',]
        # fields = ['id','date','content','image','user_id','user','replyTo','url',]


class CreateFollowSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Follow
        fields = ['id','user','following','date','url']

class FollowSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    user = PublicUserProfileSerializer(read_only=True)
    following_id = serializers.IntegerField()
    following = PublicUserProfileSerializer(read_only=True)

    class Meta:
        model = Follow
        fields = ['id','user_id','user','following_id','following','date','url']

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Like
        fields = ['id','user','message','date','url']