from django import forms

class login(forms.Form):
    username=forms.CharField(label="Username", required=True)
    password=forms.CharField(label="Password", widget=forms.PasswordInput())

class register(forms.Form):
    firstname=forms.CharField(label="First Name", required=True)
    lastname=forms.CharField(label="LastName" , required=True)
    email=forms.EmailField(label="Email", required=True)
    username=forms.CharField(label="Username", required=True)
    password=forms.CharField(label="Password", widget=forms.PasswordInput())
    confirm_password=forms.CharField(label="Confirm Password", widget=forms.PasswordInput())