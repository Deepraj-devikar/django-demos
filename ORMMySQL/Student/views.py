from django.shortcuts import render
from .models import Student

def student_info(request, *args, **kwargs):
    data = {}
    data["students"] = students = Student.objects.all()
    return render(request, "Student/student_info.html", data)
    