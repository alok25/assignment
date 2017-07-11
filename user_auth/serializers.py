from assignment.non_null_serializer import BaseSerializer
from rest_framework import serializers

from user_auth.models import User


class UserSerializer(BaseSerializer):
    """
    Serializer for registering new users.
    This class excepts users details validates them
    and returns user object.
    """
    password = serializers.CharField()

    class Meta:
        model = User
        fields = (
            'id', 'password', 'email',
            'first_name', 'last_name', 'role',)
        read_only_fields = ('id', 'password',)

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            role=validated_data['role'],
            is_active=True
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
