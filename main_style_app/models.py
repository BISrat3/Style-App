from socketserver import ThreadingUDPServer
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StoreSlide(models.Model):
    slideImg = models.CharField(max_length=250)
    title = models.CharField(max_length =200)

    def __str__(self):
        return self.title
        
class ShirtHome(models.Model):
    # template_name = "home.html"
    name = models.CharField(max_length =200)
    img = models.CharField(max_length=250)
    price =models.IntegerField()

    user = models.ForeignKey(User, on_delete = models.CASCADE, default=1)
    def __str__(self):
        return self.name
    class Meta:
        ordering =['name']

class Category(models.Model):
    name=models.CharField(max_length=200)
    Type = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete = models.CASCADE, default=1)
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]

class Products(models.Model):
    name = models.CharField(max_length=200)
    img = models.CharField(max_length=250)
    price= models.IntegerField(default=0)
    description = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

class Review(models.Model):
    comment = models.TextField(max_length=400)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='reviews')
    date = models.DateTimeField(auto_now_add=True)
    Reviewers = models.ForeignKey(User, on_delete = models.CASCADE, null=True)

    def __str__(self):
        return self.comment
     
    class Meta:
        ordering = ["-date"]