from django.shortcuts import render, redirect
from . import forms as Form
from django.contrib.auth.models import auth,User
from django.contrib.auth import authenticate

def login(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']
        return redirect("/")
    else:
        form=Form.login()
        return render(request, "user/login.html", {'form': form})

def register(request):
    if request.method=="POST":
        print()
    else: 
        form=Form.register()
        return render(request, "user/register.html", {'form': form})
# Create your views here.
def logout(request):
    return render(request, "user/register.html")