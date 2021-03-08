from rest_framework import serializers
from .models import Message
from .models import Profile
from .models import User

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','bio'
        )

class PublicUserProfileSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('id','username','first_name', 'last_name', 'profile'
        )

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    # author = PublicUserProfileSerializer(read_only=True)
    class Meta:
        model = Message
        fields = ('id','content','author'
        )