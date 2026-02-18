from rest_framework.serializers import ModelSerializer
from .models import UserAddress ,User,UserFavorite

class UserSerializer(ModelSerializer):
    class Meta:
        fields='__all__'
        model=User
class UserAddreessSerializer(ModelSerializer):
    class Meta:
        fields='__all__'
        model=UserAddress
class UserFavoriteSerializer(ModelSerializer):
    class Meta:
        fields='__all__'
        model=UserFavorite