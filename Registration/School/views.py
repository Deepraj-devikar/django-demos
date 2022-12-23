from django.shortcuts import render
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login as user_login, logout as user_logout, update_session_auth_hash
from django.http import HttpResponseRedirect 

def if_user_is_authenticated(view_function):

    def inner_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_function(request, *args, **kwargs)
        messages.error(request, "Please login first.")    
        return HttpResponseRedirect('/login/')

    return inner_function

def if_user_is_not_authenticated(view_function):

    def inner_function(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return view_function(request, *args, **kwargs)
        messages.info(request, "You are already loged in as "+request.user.username+".")
        return HttpResponseRedirect('/profile/')
    
    return inner_function 

@if_user_is_not_authenticated
def sign_up(request, *args, **kwargs):
    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            sign_up_form.save()
            messages.success(request, "Account created successfully.")
    else:
        sign_up_form = SignUpForm()
    data = {
        'form': sign_up_form,
        'title': "User Registration",
    }
    return render(request, "school/form.html", data)

@if_user_is_not_authenticated    
def login(request, *args, **kwargs):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            user = authenticate(
                username=login_form.cleaned_data['username'], 
                password=login_form.cleaned_data['password'])
            if user:
                user_login(request, user)
                messages.success(request, "Loged in successfully.")
                return HttpResponseRedirect('/profile/')
    else:
        login_form = AuthenticationForm()
    data = {
        'form': login_form,
        'title': "User Login",
    }
    return render(request, "school/form.html", data)

@if_user_is_authenticated
def profile(request, *args, **kwargs):
    data = {
        'title': "Profile",
    }
    return render(request, "school/profile.html", {})
        
def logout(request, *args, **kwargs):
    user_logout(request)
    return HttpResponseRedirect('/login/')
    
@if_user_is_authenticated
def change_password(request, *args, **kwargs):
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(user=request.user, data=request.POST)
        if password_change_form.is_valid():
            password_change_form.save()
            messages.success(request, "Password changed successfully.")
            # this function will keep you loged in
            update_session_auth_hash(request, password_change_form.user)
            # messages.info(request, "Please log in again.")
            return HttpResponseRedirect('/profile/')
    else:
        password_change_form = PasswordChangeForm(request.user)
    data = {
        'form': password_change_form,
        'title': "Change Password",
    }
    return render(request, "school/form.html", data)

def not_found(request, path):
    data = {
        'path': path
    }
    return render(request, "school/not_found.html", data)
    