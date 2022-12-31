from django.shortcuts import render, redirect
from .forms import seller_form
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def car_data(request):
    global isLogin
    if request.method == 'POST':
        print(request.FILES["images"])
        form=seller_form(request.POST, request.FILES)
        print(request.FILES['images'])
        if form.is_valid():
            # car.CarCompany=request.POST["carCompany"]
            # car.carName=request.POST["carName"]
            # car.manu_Date=request.POST["manu_Date"]
            # car.kilometers=request.POST["kilometers"]
            # car.Fuel_type=request.POST["Fuel_type"]
            # car.color=request.POST["color"]
            # car.first_owner=request.POST["first_owner"]
            # car.expected_price=request.POST["expected_price"]
            # car.car_insurance=request.POST["car_insurance"]
            # car.insurance_type=request.POST["insurance_type"]
            # car.car_registration_no=request.POST["car_registration_no"]
            # car.images=request.FILES["images"] 
            form.save()
            print("The form data is stored")
            return redirect("/")
        else:
            return render(request, "seller/seller_data.html", {'form': form})
    else:
        form= seller_form()
        return render(request, "seller/seller_data.html", {'form': form})
def login(request):
    return render(request, "user/login.html")