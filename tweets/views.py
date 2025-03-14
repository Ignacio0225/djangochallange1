from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tweet
from .seralizers import TweetSerializer

# Create your views here.

class Tweets(APIView):
    def get(self,request):
        all_tweets = Tweet.objects.all()
        serializer = TweetSerializer(all_tweets, many = True)
        return Response(serializer.data)

