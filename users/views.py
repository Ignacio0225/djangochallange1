from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.exceptions import NotAuthenticated
from .models import User
from .serializer import UserSerializer
from tweets.seralizers import TweetSerializer


# Create your views here.

class Users(APIView):
    def get(self,request):
        all_users = User.objects.all()
        serializer = UserSerializer(all_users,many=True)
        return Response(serializer.data)

class UserDetail(APIView):

    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound

    def get(self,request,pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class UserTweet(APIView):

    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound

    def get(self,request,pk):
        # user = self.get_object(pk)

        if request.user.is_authenticated:
            try:
                page = request.query_params.get('page',1)
                page = int(page)
            except ValueError:
                page = 1

            page_size = 5
            start = (page - 1) * page_size
            end = start + page_size

            user = self.get_object(pk)
            serializer = TweetSerializer(
            user.tweets.all()[start:end],
                many=True,
            )
            return Response(serializer.data)

        raise NotAuthenticated
