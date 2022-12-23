from django import forms
from .models import *

class StudentRegistrationModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'password']