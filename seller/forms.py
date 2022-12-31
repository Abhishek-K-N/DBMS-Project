from django import forms
from django.forms import ModelForm
from .models import Car

class seller_form(ModelForm):
    carCompany=forms.CharField(label="Car Manufacturer", max_length=15, required=True)
    carName=forms.CharField(max_length=15,required=True, label="Car Name")
    manu_Date=forms.DateField(required=True, label="Manufactured Date")
    kilometers=forms.IntegerField(label="Distance Travelled(in KM)", required=True)
    Fuel_type=forms.CharField(label="Fuel Type", widget=forms.Select(choices=(("Petrol", "Petrol"), ("Diesel", "Diesel"), ("EV", "EV"))), required=True)
    color=forms.CharField(max_length=10, label="Car Colour", required=True)
    first_owner=forms.BooleanField(label="First Owner", required=True)
    expected_price=forms.IntegerField(label="Expected Price")
    car_insurance=forms.BooleanField(label="Car Insurance", required=True)
    insurance_type=forms.CharField(max_length=15, label="Insurance Type")
    car_registration_no=forms.CharField(max_length=10, label="Registration Number", required=True)
    images=forms.ImageField(label="Car Images", required=True)
    class Meta:
        model =Car
        fields=['carCompany', 'carName', 'manu_Date', 'kilometers', 'Fuel_type', 'color', 'first_owner', 'expected_price',
        'car_insurance', 'insurance_type', 'car_registration_no','images']
