from collections import UserList
from django.shortcuts import render, redirect
from .forms import seller_form
from .models import Car
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from user.models import UserProfile


# Create your views here.
@login_required(login_url='login')
def car_data(request):
    global isLogin
    if request.method == 'POST':
        carCompany=request.POST['carCompany']
        carName=request.POST['carName']
        manu_Date=request.POST['manu_Date']
        kilometers=request.POST['kilometers']
        Fuel_type=request.POST['Fuel_type']
        color=request.POST['color']
        expected_price=request.POST['expected_price']
        insurance_type=request.POST['insurance_type']
        car_registration_no=request.POST['car_registration_no']
        images=request.FILES['images']
        car_data=Car(carCompany=carCompany, carName=carName, manu_Date=manu_Date, kilometers=kilometers, 
        Fuel_type=Fuel_type, color=color, expected_price=expected_price, insurance_type=insurance_type, car_registration_no=car_registration_no, images=images)
        print(car_data)
        car_data.save()
        user=User.objects.get(username=request.user)
        profile=UserProfile.objects.get(user_info=user)
        profile.selled_car=car_data
        profile.save()
        print("The form data is stored")
        return redirect("/")
    else:
        form= seller_form()
        return render(request, "seller/seller_data.html", {'form': form})
def login(request):
    return render(request, "user/login.html")