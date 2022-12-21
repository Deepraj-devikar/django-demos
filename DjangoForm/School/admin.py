from django.contrib import admin
from .models import *

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_name', 'teacher_email', 'roll_number', 'password')

admin.site.register(Teacher, TeacherAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'student_email', 'roll_number', 'password')

admin.site.register(Student, StudentAdmin)
