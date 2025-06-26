from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    address=models.TextField()
    profilePicture=models.ImageField()
    user = models.OneToOneField(User, on_delete=models.CASCADE) #User--built in user model from django.contrib.auth.models 
