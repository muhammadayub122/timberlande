from django.urls import path
from .views import CategoryListcreateView,ProductListcreateView

urlpatterns = [
    path('product/',ProductListcreateView.as_view()),
    path('category/',CategoryListcreateView.as_view()),

]
