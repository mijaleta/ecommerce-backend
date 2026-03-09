from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)   
    phone_number = models.CharField(max_length=20, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = []   

    
    def __str__(self):
        return self.email