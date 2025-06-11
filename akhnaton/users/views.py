from django.shortcuts import render

from users.forms import LoginForm

# Create your views here.

def Login(request):
    form = LoginForm()
    return render(request,'users/login.html',{'form':form})