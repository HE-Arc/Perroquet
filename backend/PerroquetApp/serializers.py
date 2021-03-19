from rest_framework import serializers
from .models import Message
from .models import Profile
from .models import User
from django.db import models

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','bio'
        )

class PublicUserProfileSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('id','username','first_name', 'last_name', 'profile','url'
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','password','url')

        # fields = '__all__'

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    author = PublicUserProfileSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True)

    class Meta:
        model = Message
        fields = ['id','content','author_id','author','replyTo','url',]
        # depth=1