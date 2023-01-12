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
    password1=forms.CharField(label="Confirm Password", widget=forms.PasswordInput())
    gender=forms.CharField(label="Gender", widget=forms.Select(choices=(("Male", "Male"), ("Female", "Female"), ("NA", "NA"))), required=True)
    dob=forms.CharField(label="Date of Birth", required=True)
    address=forms.CharField(label="Address", required=True)
    contact_no=forms.CharField(label="Contact Number", required=True)