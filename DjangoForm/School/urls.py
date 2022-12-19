from django.urls import path
from .views import *

urlpatterns = [
    path('person_form/', person_form)
]