from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,DestroyAPIView
from .models import UserAddress , UserFavorite
from .serializer import UserAddreessSerializer,UserFavoriteSerializer
from rest_framework.permissions import IsAuthenticated
from config.paginator import MyPaginator
# Create your views here.
from rest_framework.response import Response
class UserAddressListCreateApiView(ListCreateAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddreessSerializer
    permission_classes = [IsAuthenticated]
    pagination_class=MyPaginator
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def create(self, request):
         self.request.data['user'] = self.request.user.id
         return super().create(self.request)


class UserFavoriteListCreateApiView(ListCreateAPIView):
    queryset = UserFavorite.objects.all()
    serializer_class = UserFavoriteSerializer
    permission_classes = [IsAuthenticated]
    pagination_class=MyPaginator

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def create(self, request):
         self.request.data['user'] = self.request.user.id
         return super().create(self.request)
    
class UserFavoriteDestroyApiView(DestroyAPIView):
    queryset = UserFavorite.objects.all()
    serializer_class = UserFavoriteSerializer
    permission_classes = [IsAuthenticated]

def perform_destroy(self, instance):
        if isinstance.user == self.request.user:
            return super().perform_destroy(instance)
        return False

      