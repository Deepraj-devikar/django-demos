from django.shortcuts import render
from .forms import *
from django.contrib import messages

def student_registration(request):
    if request.method == 'POST':
        student_registration_form = StudentRegistrationModelForm(request.POST)
        if student_registration_form.is_valid():
            student_registration_form.save()
            messages.add_message(request, messages.SUCCESS, "Your registration have been successful.")
            messages.info(request, "Now you can log in.")
    else:
        student_registration_form = StudentRegistrationModelForm()
    data = {
        'student_registration_form': student_registration_form
    }
    print(messages.get_level(request))
    # Levels according to message tag
    # Debug => 10
    # Info => 20
    # Success => 25
    # Warning => 30
    # Error => 40
    # we can manually set levels 
    # messages.set_level(request, [messages.DEBUD | messages.INFO | messages.SUCCESS | messages.WARNING | messages.ERROR])
    return render(request, 'school/student_registration.html', data)
    