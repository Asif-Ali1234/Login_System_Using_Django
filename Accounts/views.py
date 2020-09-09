from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib import auth,messages

from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.method=="POST":
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]
        email=request.POST["email"]
        password=request.POST["passwd"]

        password2=request.POST["cnfrmpasswd"]

        if User.objects.filter(username=email).exists():
            messages.error(request,"User already exists try login if you dont know the password try deleting account and recreate")
            return redirect('register')

        elif password != password2:
            messages.error(request,'Passwords not matched')
            return redirect('register')

        else:
            user=User.objects.create_user(username=email,first_name=firstname,last_name=lastname,email=email,password=password)
            user.save()
            messages.success(request,"Login succesfull")
            return redirect('login')
    else:
        return render(request,'register.html')



def login(request):
    if request.method=="POST":
        usrnm=request.POST["email"]
        passwd=request.POST['passwd']
        user=auth.authenticate(username=usrnm,password=passwd)
        if user is None:
            messages.error(request,"Not matched")
            return redirect('login')
        else:
            auth.login(request,user)
            messages.success(request,"Logged in successfully")
            return redirect("/")

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    messages.success(request,'Logged out')
    return redirect('/')

