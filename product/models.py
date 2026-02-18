from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=233)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=233)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True,null=True)
    price = models.PositiveBigIntegerField(default=0)
    current_price = models.PositiveSmallIntegerField(default=0)
    image = models.ImageField(upload_to='products/' , blank=True,null=True)
    discount = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.title
