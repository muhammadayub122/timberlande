from rest_framework.serializers import ModelSerializer
from .models import Category,Product

class CategorySerializer(ModelSerializer):
    class Meta:
        fields='__all__'
        model=Category
class ProductSerializer(ModelSerializer):
    class Meta:
        fields='__all__'
        model=Product
    