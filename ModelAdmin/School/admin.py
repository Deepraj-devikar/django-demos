from django.contrib import admin
from .models import *

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'roll_number', 'student_name', 'student_email')

# admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher)