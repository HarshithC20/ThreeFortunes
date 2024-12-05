from django.db import models
from django.contrib.auth.models import AbstractUser

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

# Food Name
# Category(Starter, Main course, Dessert, Snacks)
# Price
# Image