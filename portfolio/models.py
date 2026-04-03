from django.db import models

# Create your models here.
class Product(models.Model):
    name= models.CharField(max_length=100)
    description= models.TextField()
    price= models.FloatField()
    created_at= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Profile(models.Model):
    name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to="profile_pics/")

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name    

    
    
