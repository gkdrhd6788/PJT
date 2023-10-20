from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm


@require_http_methods(['GET','POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect("boards:index")
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect("boards:index")
        
    else:
        form = CustomUserCreationForm()
    context =  {

        'form':form,
    }
    return render(request,'accounts/signup.html',context)

@require_http_methods(['GET','POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect("boards:index")
    

    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect("boards:index")
        
    else:
        form = AuthenticationForm()
    context =  {

        'form':form,
    }
    return render(request,'accounts/login.html',context)

@require_http_methods(['POST'])
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("boards:index") 
    