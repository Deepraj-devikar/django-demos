from django.shortcuts import render
from .forms import *

def add(request, *args, **kwargs):
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
    student_form = StudentForm()    
    return render(request, "school/add.html", {"student_form": student_form})
    
