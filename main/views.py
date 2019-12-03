from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# from django.http import *
from .forms import loginform,registerform
from .models import *
from django.core.exceptions import ValidationError
from django.contrib import messages
# from django.contrib import auth
# from django.contrib.auth import authenticate
from django.views.generic import ListView
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    context= {}
    return render(request,'index.html', context)

def register(request):
    if request.method=='POST':
        form= registerform(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            first_name= form.cleaned_data.get('first_name')
            last_name= form.cleaned_data.get('last_name')
            email= form.cleaned_data.get('email')
            password= form.cleaned_data.get('password')
            cpassword = form.cleaned_data.get("confirm_password")
            user = User.objects.create_user(username=username, first_name= first_name, last_name =last_name, email=email, password=password)
            user.save(); 
            messages.success(request,'Registered successfully..Login here')
            return redirect('/login/')
            # if password == cpassword:
                # if User.objects.filter(username= username).exists():
                    # messages.error(request,'Username already exist')
                    # return HttpResponseRedirect('/register/')
            # else:
            #     messages.error(request,'Password not matched')
            #     return redirect ('/register/')                
    # else:
        # form= registerform()
    return render (request, 'register.html', {'form': registerform})

def login(request):
    if request.method=='POST':
        form=loginform(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            password= form.cleaned_data['password']
            try:
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    return redirect ('/profile/')
                else: 
                    messages.warning(request,'Invalid Credentials')

            except ObjectDoesNotExist:
                print("invalid user")  
    # else:
    #     form= loginform() 

    return render (request,'login.html', context={'form': loginform})

class profile(ListView):
    model= User
    template_name= 'profile.html'
    context_object_name = 'obj'




