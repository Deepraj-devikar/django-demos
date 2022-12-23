from django.shortcuts import render
from .forms import *
from django.contrib import messages

def student_registration(request):
    if request.method == 'POST':
        student_registration_form = StudentRegistrationModelForm(request.POST)
        if student_registration_form.is_valid():
            student_registration_form.save()
            messages.add_message(request, messages.SUCCESS, "Your registration have been successful")
    else:
        student_registration_form = StudentRegistrationModelForm()
    data = {
        'student_registration_form': student_registration_form
    }
    return render(request, 'school/student_registration.html', data)
    