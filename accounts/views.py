from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request,'user already exist')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'email already exist')
            return redirect('/')
        else:
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()
            return redirect('register')
    else:
        return render(request,'register.html')


def login(request):
  if request.method=='POST':
      username=request.POST['username']
      password=request.POST['password']
      user=auth.authenticate(username=username,password=password)
      if user is not None:
          return redirect('/')
      else:
          messages.info(request,'invalid login')
          return redirect('login')

  return render(request,'login.html')




def logout(request):
    auth.logout(request)
    return render('/')

