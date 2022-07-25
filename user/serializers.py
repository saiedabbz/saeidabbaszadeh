from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User, UserAddress



class UserAddressManySerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAddress
        fields = (
            "id",
            "title",
            "addr",
            "full_name",
            "mobile",
            "created_at",
        )


class UserAddressOneSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAddress
        fields = (
            "id",
            "title",
            "addr",
            "state",
            "city",
            "postal_code",
            "national_code",
            "full_name",
            "mobile",
            "created_at",
        )


class UserSerializer(serializers.ModelSerializer):
    addresses = UserAddressManySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "addresses",
        )



class TokenObtainLifetimeSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['lifetime'] = int(refresh.access_token.lifetime.total_seconds())
        data['user'] = UserSerializer(self.user).data
        return {
            'data': data,
            'message': '',
            'success': True
        }


class TokenRefreshLifetimeSerializer(TokenRefreshSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = RefreshToken(attrs['refresh'])
        data['lifetime'] = int(refresh.access_token.lifetime.total_seconds())
        data['user'] = UserSerializer(self.user).data
        return {
            'data': data,
            'message': '',
            'success': True
        }


