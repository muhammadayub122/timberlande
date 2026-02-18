from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user-address/', views.UserAddressListCreateApiView.as_view()),
    path('user-favourite/', views.UserFavoriteListCreateApiView.as_view()),
    path('user-favourite/<int:pk>/', views.UserFavoriteDestroyApiView.as_view()),
]
