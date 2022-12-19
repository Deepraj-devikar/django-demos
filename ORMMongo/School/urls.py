from django.urls import path
from .views import *

urlpatterns = [
    path('student_info/', student_info)
]