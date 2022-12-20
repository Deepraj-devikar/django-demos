from django.urls import path
from .views import *

urlpatterns = [
    path('person_form/', person_form),
    path('person_info/', person_info, name="person_info")
]