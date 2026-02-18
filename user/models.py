from django.db import models
from django.contrib.auth.models import AbstractUser
from product.models import Product
# Create your models here.


class User(AbstractUser):
    phone_number = models.CharField(max_length=20,blank=True,null=True)
    language = models.CharField(max_length=4,default='uz')

    def __str__(self):
        return f"{self.username}"
    



class UserFavorite(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} | {self.product}"
    

class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_name = models.CharField(max_length=234)
    created_at = models.DateTimeField(auto_now_add=True)
    longitude = models.CharField(max_length=344)
    latetude = models.CharField(max_length=344)

    def __str__(self):
        return f"{self.user} | {self.address_name}"
