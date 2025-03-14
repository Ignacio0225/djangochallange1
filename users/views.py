from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from .models import User
from .serializer import UserSerializer


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