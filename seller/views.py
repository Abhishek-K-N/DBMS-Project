from django.shortcuts import render
from . import forms

# Create your views here.
def car_data(request):
    if request.method == 'POST':
        car_company=request.POST['carCompany']
        print(car_company)
    else:
        form= forms.seller_form()
        return render(request, "seller/seller_data.html", {'form': form})
def login(request):
    return render(request, "user/login.html")