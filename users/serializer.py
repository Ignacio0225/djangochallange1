from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'avatar',
            'name',
        )

class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            'id',
            'password',
            'is_superuser',
            'is_staff',
            'is_active',
            'first_name',
            'last_name',
            'user_permissions',
            'groups',
        )