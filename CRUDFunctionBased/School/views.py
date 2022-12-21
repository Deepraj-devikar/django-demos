from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *

def add_update(request, id = None):
    if id is not None:
        student = Student.objects.get(pk = id)
        to_do_action = "Update"
    else:
        student = None
        to_do_action = "Add"
    if request.method == 'POST':
        student_form = StudentForm(request.POST, instance = student)
        if student_form.is_valid():
            student_form.save()
            return HttpResponseRedirect(reverse('show'))
    else:
        student_form = StudentForm(instance = student)
    data = {"student_form": student_form, "to_do_action": to_do_action}
    print(data)
    return render(request, "school/add_update.html", data)
    
def show(request):
    students = Student.objects.all()
    return render(request, "school/show.html", {"students": students})
    
def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk = id)
        student.delete()
        return HttpResponseRedirect(reverse('show'))
        
