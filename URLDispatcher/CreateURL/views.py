from django.shortcuts import render

def welcome(request, *args, **kwargs):
    return render(request, "createurl/welcome.html", kwargs)

def welcome_to_home(request, *args, **kwargs):
    return render(request, "createurl/welcome_to_home.html", kwargs)