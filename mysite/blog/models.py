from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    
    def __str__(self):
        return self.title


class Customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    
    def __str__(self):
        return self.name
    
# class Product(models.Model):
#     product_cat = models.CharField(max_length=30)
#     product_item = models.CharField(max_length=20)
    
#     def __str__(self):
#         return self.product_cat
    
class myfriends(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    address = models.TextField(max_length=30)
    email = models.EmailField()
    photo = models.ImageField(upload_to='photo')
    created = models.DateField()
    
    def __str__(self):
        return self.name