from django.shortcuts import render
from .forms import *

def sign_up(request):
    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            sign_up_form.save()
    else:
        sign_up_form = SignUpForm()
    data = {
        'sign_up_form': sign_up_form
    }
    return render(request, "school/sign_up.html", data)
    