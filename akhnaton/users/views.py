from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login
from users.forms import LoginForm

# Create your views here.

def user_login(request):
    error_message = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,username=data['username'],password=data['password'])
            if user is not None:
                login(request,user)
                if user.username== 'farid':
                    return redirect('/admin/')
                else:
                    return redirect('index')
            else:
                error_message = "username or password are incorrect"
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {
        'form': form,
        'error_message': error_message
    })


def forbidden(request):
    return render(request,'users/forbidden.html')