from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView
from .models import Product,Category
from .serailizer import CategorySerializer,ProductSerializer
from config.paginator import MyPaginator
# Create your views here.
class  ProductListcreateView(ListCreateAPIView):
    queryset=Product
    serializer_class=ProductSerializer
    pagination_class=MyPaginator
class  CategoryListcreateView(ListCreateAPIView):
    queryset=Category
    serializer_class=CategorySerializer
    pagination_class=MyPaginator