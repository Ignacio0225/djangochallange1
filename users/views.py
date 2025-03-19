from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound, ParseError
from rest_framework.views import APIView
from rest_framework.exceptions import NotAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import User
from .serializer import UserSerializer, CreateUserSerializer
from tweets.seralizers import TweetSerializer


# Create your views here.

class Users(APIView):
    def get(self,request):
        all_users = User.objects.all()
        serializer = UserSerializer(all_users,many=True)
        return Response(serializer.data)

    def post(self,request):
        password = request.data.get('password')
        if not password:
            raise ParseError
        serializer = CreateUserSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            serializer=CreateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class UserDetail(APIView):

    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound

    def get(self,request,pk):
        user = self.get_object(pk)
        serializer = CreateUserSerializer(user)
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

class ChangePW(APIView):

    permission_classes = [IsAuthenticated]

    def put(self,request):
        user = request.user
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        if not old_password or not new_password:
            raise ParseError
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response(status=HTTP_200_OK)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)

class LogIn(APIView):
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        if not username or not password:
            raise ParseError
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user:
            login(request,user)
            return Response({"confirm":"you are loged in"})
        else:
            return Response({"error":"check your ID or PW"})

class LogOud(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        logout(request)
        return Response({"confirm":"see you again"})
