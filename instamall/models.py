from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # stores

# class Vendor(models.Model):
#     username = models.CharField(max_length=50)
#     company_name = models.CharField(max_length=50)
#     owner = models.OneToOneField(User, related_name="vendor", on_delete=models.CASCADE)
#     email = models.EmailField(max_length=254)
#     password = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class Mall(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    user = models.ForeignKey(User, related_name="malls", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # stores

class Store(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    malls = models.ManyToManyField(Mall, related_name="stores")
    vendor = models.ForeignKey(User, related_name="stores", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # products

class Product(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.URLField(max_length=200,default="")
    price = models.FloatField()
    stock_quantity = models.IntegerField()
    store = models.ForeignKey(Store, related_name="products", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)