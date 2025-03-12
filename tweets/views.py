from http.client import HTTPResponse
from .models import Tweet
from django.shortcuts import render

# Create your views here.

def tweet(request):
    tweets = Tweet.objects.all()
    return render(request,'tweet.html',{'tweets':tweets,"title":"DjangoChallenge"})