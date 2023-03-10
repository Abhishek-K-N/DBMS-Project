from django.shortcuts import render, redirect
from . import forms as Form
from django.contrib.auth.models import auth,User
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import UserProfile
from django.contrib import messages

def login(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)
        if(user is not None):
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid Credentials")
            return redirect("login")
    else:
        form=Form.login()
        return render(request, "user/login.html", {'form': form})

def register(request):
    if request.method == 'POST':
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        user_name=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        dob=request.POST["dob"]
        address=request.POST["address"]
        contact=request.POST["contact_no"]
        gender=request.POST["gender"]
        if password==password1:
            user=User.objects.create_user(first_name=first_name, last_name=last_name, username=user_name, email=email, password=password)
            user.save()
            userprofile=UserProfile(user_info=user, gender=gender, dob=dob, Address=address, contact_number=contact)
            userprofile.save()
            print("User created")
            return redirect("/") 
        else:
            messages.info(request, "Password doesn't match")
            return redirect("register")
    else: 
        form=Form.register()
        return render(request, "user/register.html", {'form': form})

# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect("/")