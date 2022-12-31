from django.shortcuts import render
from seller.models import Car


# Create your views here.
def buy(request):
    Cars=Car.objects.all()
    return render(request, "buyer/buy.html", {'Cars': Cars})
