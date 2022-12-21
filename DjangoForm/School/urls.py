from django.urls import path
from .views import *

urlpatterns = [
    path('person_form/', person_form),
    path('person_info/', person_info, name="person_info"),
    path('student_form/', student_model_form),
    path('student_info/', student_info, name="student_info"),
    path('student_delete/', student_delete),
    path('teacher_form/', teacher_model_form),
    path('teacher_info/', teacher_info, name="teacher_info"),
    path('teacher_delete/', teacher_delete),
]