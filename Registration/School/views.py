from django.shortcuts import render
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.http import HttpResponseRedirect 

def sign_up(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/profile/')
    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            sign_up_form.save()
            messages.success(request, "Account created successfully.")
    else:
        sign_up_form = SignUpForm()
    data = {
        'form': sign_up_form,
        'title': "User Registration"
    }
    return render(request, "school/form.html", data)
    
def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/profile/')
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            user = authenticate(
                username=login_form.cleaned_data['username'], 
                password=login_form.cleaned_data['password'])
            if user:
                user_login(request, user)
                return HttpResponseRedirect('/profile/')       
    else:
        login_form = AuthenticationForm()
    data = {
        'form': login_form,
        'title': "User Login"
    }
    return render(request, "school/form.html", data)

def profile(request):
    if request.user.is_authenticated:
        return render(request, "school/profile.html", {})
    return HttpResponseRedirect('/login/')
        
def logout(request):
    user_logout(request)
    return HttpResponseRedirect('/login/')
    