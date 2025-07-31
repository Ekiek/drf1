from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()

class Address(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
