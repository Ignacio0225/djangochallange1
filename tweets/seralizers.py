from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Tweet
from users.serializer import UserSerializer



class TweetSerializer(ModelSerializer):

    user = serializers.CharField(read_only=True)

    class Meta:
        model = Tweet
        fields = '__all__'