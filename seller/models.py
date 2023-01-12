from django.db import models
# Create your models here.
class Car(models.Model):
    id=models.AutoField(primary_key=True)
    carCompany=models.CharField(max_length=15)
    carName=models.CharField(max_length=15)
    manu_Date=models.DateField()
    kilometers=models.IntegerField()
    Fuel_type=models.CharField(max_length=10)
    color=models.CharField(max_length=10)
    expected_price=models.IntegerField()
    insurance_type=models.CharField(max_length=15)
    car_registration_no=models.CharField(max_length=10)
    images=models.ImageField(upload_to="Images")

    

