from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *
from .models import *

def person_form(request, *args, **kwargs):
    data = {}
    if request.method == 'POST':
        personForm = PersonForm(request.POST)
        if personForm.is_valid():
            print("Form Validated")
            for formField, formFieldValue in personForm.cleaned_data.items():
                print(formField+" => "+str(formFieldValue))
            url = reverse("person_info")
            return HttpResponseRedirect(url)        
            # return render(request, "School/person_info.html", data)
    else:
        personForm = PersonForm(
            auto_id = "some_%s", 
            label_suffix = " Some :-  ",
            initial={"name": "Ganesh", "age": 20}
        )
        #-----------------auto_id-----------------
        # auto_id by default 'id_%s',
        # if we make auto_id = True or any other value which dont have %s like 'some' then it will be '%s'
        # if we make auto_id = False then it wiil not show id it will be ''
        #-----------------label_suffix---------------
        # label_sufix by default ':' we can change it by providing string
        #-----------------intial---------------------
        # for setting initial values of fields
        # we can use it in edit page
    personForm.order_fields(["name", "first_name"])
    # we can set fields order
    # if some fields not included in order_fields then that remaining feilds will follow default order after mentioned fields
    data["personForm"] = personForm
    return render(request, "School/person_form.html", data)

def person_info(request, *args, **kwargs):
    return render(request, "School/person_info.html", {})

def student_form(request, *args, **kwargs):
    data = {}
    if request.method == 'POST':
        studentForm = StudentForm(request.POST)
        if studentForm.is_valid():
            print("Form Validated")
            for formField, formFieldValue in studentForm.cleaned_data.items():
                print(formField+" => "+str(formFieldValue))
            student_data = studentForm.cleaned_data
            student = Student(
                id = 1, # for update id is given
                student_name = student_data['student_name'],
                student_email = student_data['student_email'],
                roll_number = student_data['roll_number'],
                password = student_data['password']
            )
            student.save()
            url = reverse("student_info")
            return HttpResponseRedirect(url)
    else:
        studentForm = StudentForm()
    data["studentForm"] = studentForm
    return render(request, "School/student_form.html", data)

def student_model_form(request, *args, **kwargs):
    data = {}
    if request.method == 'POST':
        studentForm = StudentModelForm(request.POST)
        if studentForm.is_valid():
            print("Form Validated")
            for formField, formFieldValue in studentForm.cleaned_data.items():
                print(formField+" => "+str(formFieldValue))
            student_data = studentForm.cleaned_data
            student = Student(
                id = 1, # for update id is given
                student_name = student_data['student_name'],
                student_email = student_data['student_email'],
                roll_number = student_data['roll_number'],
                password = student_data['password']
            )
            student.save()
            url = reverse("student_info")
            return HttpResponseRedirect(url)
    else:
        studentForm = StudentModelForm()
    data["studentForm"] = studentForm
    return render(request, "School/student_form.html", data)

def student_info(request, *args, **kwargs):
    return render(request, "School/student_info.html", {})

def student_delete(request, *args, **kwargs):
    student = Student(id = 1)
    student.delete()
    return HttpResponseRedirect("/admin/School/student")

def teacher_form(request, *args, **kwargs):
    data = {}
    if request.method == 'POST':
        teacherForm = TeacherForm(request.POST)
        if teacherForm.is_valid():
            print("Form Validated")
            for formField, formFieldValue in teacherForm.cleaned_data.items():
                print(formField+" => "+str(formFieldValue))
            teacher_data = teacherForm.cleaned_data
            teacher = Teacher(
                id = 1, # for update id is given
                teacher_name = teacher_data['teacher_name'],
                teacher_email = teacher_data['teacher_email'],
                password = teacher_data['password'],
                roll_number = teacher_data['roll_number']
            )
            teacher.save()
            url = reverse("teacher_info")
            return HttpResponseRedirect(url)
    else:
        teacherForm = TeacherForm()
    data["teacherForm"] = teacherForm
    return render(request, "School/teacher_form.html", data)

def teacher_model_form(request, *args, **kwargs):
    data = {}
    if request.method == 'POST':
        teacherForm = TeacherModelForm(request.POST)
        if teacherForm.is_valid():
            print("Form Validated")
            for formField, formFieldValue in teacherForm.cleaned_data.items():
                print(formField+" => "+str(formFieldValue))
            teacher_data = teacherForm.cleaned_data
            teacher = Teacher(
                id = 1, # for update id is given
                teacher_name = teacher_data['teacher_name'],
                teacher_email = teacher_data['teacher_email'],
                password = teacher_data['password'],
                roll_number = teacher_data['roll_number']
            )
            teacher.save()
            url = reverse("teacher_info")
            return HttpResponseRedirect(url)
    else:
        teacherForm = TeacherModelForm()
    data["teacherForm"] = teacherForm
    return render(request, "School/teacher_form.html", data)

def teacher_info(request, *args, **kwargs):
    return render(request, "School/teacher_info.html", {})

def teacher_delete(request, *args, **kwargs):
    teacher = Teacher(id = 1)
    teacher.delete()
    return HttpResponseRedirect("/admin/School/teacher")