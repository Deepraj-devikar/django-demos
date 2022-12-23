from django.shortcuts import render
from .forms import *

def student_registration(request):
    if request.method == 'POST':
        student_registration_form = StudentRegistrationModelForm(request.POST)
        if student_registration_form.is_valid():
            student_registraion_form.save()
            # message.success(request, "Your registration have been successful")
    else:
        student_registration_form = StudentRegistrationModelForm()
    data = {
        'student_registration_form': student_registration_form
    }
    return render(request, 'school/student_registration.html', data)
    