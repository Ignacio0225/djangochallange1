from functools import partial

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotAuthenticated, NotFound, PermissionDenied
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Tweet
from .seralizers import TweetSerializer

# Create your views here.

class Tweets(APIView):
    def get(self,request):
        all_tweets = Tweet.objects.all()
        serializer = TweetSerializer(all_tweets, many = True)
        return Response(serializer.data)

    def post(self,request):
        if request.user.is_authenticated:
            serializer = TweetSerializer(
                data=request.data,
                many=True,
            )
            if serializer.is_valid():
                tweets = serializer.save()
                return Response(TweetSerializer(tweets).data)
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


class TweetDetail(APIView):

    def get_object(self,pk):
        try:
            return Tweet.objects.get(pk = pk)
        except Tweet.DoesNotExist:
            raise NotFound


    def get(self,request,pk):
        tweet = self.get_object(pk)
        serializer = TweetSerializer(tweet)
        return Response(serializer.data)

    def put(self,request,pk):

        tweet = self.get_object(pk)

        if not request.user.is_authenticated:
            raise NotAuthenticated

        if tweet.user != request.user:
            raise PermissionDenied

        serializer = TweetSerializer(
            tweet,
            data = request.data,
            partial=True,
        )
        if serializer.is_valid():
            tweet = serializer.save()
        return Response(TweetSerializer(tweet).data)

    def delete(self,request,pk):
        tweet = self.get_object(pk)

        if not request.user.is_authenticated:
            raise NotAuthenticated
        if tweet.user != request.user:
            raise PermissionDenied

        tweet.delete()
        return Response(HTTP_204_NO_CONTENT)
