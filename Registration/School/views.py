from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def sign_up(request):
    if request.method == 'POST':
        user_creation_form = UserCreationForm(request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
    else:
        user_creation_form = UserCreationForm()
    data = {
        'user_creation_form': user_creation_form
    }
    return render(request, "school/sign_up.html", data)
    