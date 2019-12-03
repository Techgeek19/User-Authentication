from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.shortcuts import redirect

class registerform(forms.ModelForm):
    username= forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input-field','placeholder': 'Enter Username'}), 
        required= True, max_length=50) 
    email= forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'input-field','placeholder': 'Enter Email'}),   
        required= True, max_length=50)
    first_name= forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input-field','placeholder': 'Enter First Name'}),
        required= True, max_length=50)
    last_name= forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input-field','placeholder': 'Enter Last Name'}),
        required= True, max_length=50)
    password= forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input-field','placeholder': 'Enter Password'}),
        required= True, max_length=50)
    confirm_passsword= forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input-field','placeholder': 'Confirm Password'}),
        required= True, max_length=50)

    class Meta():
        model= User
        fields= ['username', 'email','first_name', 'last_name', 'password']
    
    # def clean_username(self):
    #     user= self.cleaned_data['username']
    #     if user== User.objects.get(username= user):
    #         return self.cleaned_data['username']
    #     else:
    #         messages.warning(request,'Username already exist')

    # def clean_password(self):
    #     password= self.cleaned_data.get('password')
    #     cpassword= self.cleaned_data.get('confirm_password')
    #     MIN_LENGTH= 8
    #     if password and cpassword:
    #         if password != cpassword:
    #             messages.warning(request,'Passwords not matched')
    #             return redirect ('/register/')
    #         else:
    #             if len(password) < MIN_LENGTH:
    #                 messages.warning(request,'Password length must contains atleast 8 characters')
    #                 # print('Password length must contains atleast %d characters' %MIN_LENGTH)
    #             if pas.isdigit():
    #                 messages.warning(request,'Password must not contains all numeric character')


class loginform(forms.Form):
    username= forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input-field','placeholder': 'Enter Username'}), 
        required= True, max_length=50) 
    password= forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input-field','placeholder': 'Enter Password'}),
        required= True, max_length=150)


    
