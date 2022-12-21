from django import forms 
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'password']
        # we can give values to fields like '__all__' it will take all fields of model
        # one more attribute 'exclude' it will take list or tuple of that fields which vahe to exclude from form 
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(render_value = True, attrs={'class': 'form-control'})
        }

# we can inherit one form into another form 
# both forms model form or both forms are normal forms 
# or parent form is model form and child form is normal form and vice versa