
from http.client import HTTPResponse
from .models import User
from django.shortcuts import render

# Create your views here.

def user(request,pk):
    try:
        user_pk = User.objects.get(pk=pk)
        user_tweet = user_pk.tweets.all()
        return render(request,'users.html',{'user_tweet':user_tweet,"title":"DjangoChallenge2"})
    except User.DoesNotExist: #User 는 모델에서 가져오는거 모델이 없으면 이라는거임
        return render(request,"users.html", {"not_found": True})