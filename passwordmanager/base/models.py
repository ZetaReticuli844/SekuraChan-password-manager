from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def __str__(self):
        return self.email
   


class PasswordEntry(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    website = models.CharField(max_length=100)
    website_user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    additional_info = models.CharField(max_length=100)
    def __str__(self):
        return self.website
    
class home(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.email



    
    

    
    