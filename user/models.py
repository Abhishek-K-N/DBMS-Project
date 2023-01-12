from django.db import models
from django.contrib.auth.models import User
from seller.models import Car

class User_details(models.Model):
    user_info=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True),
    dob=models.DateField()
    Address=models.CharField(max_length=100)
    contact_number=models.CharField(max_length=14)
    selled_car=models.ForeignKey(Car, on_delete=models.CASCADE, null=True)

class UserProfile(models.Model):
    user_info=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    gender=models.CharField(max_length=10, null=True)
    dob=models.DateField(null=True)
    Address=models.CharField(max_length=100, null=True)
    contact_number=models.CharField(max_length=14, null=True)
    selled_car=models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    


# Create your models here.
