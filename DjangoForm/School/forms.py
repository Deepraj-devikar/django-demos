from django import forms 
from django.core import validators
from .models import *

GEEKS_CHOICES =(
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
    ("4", "Four"),
    ("5", "Five"),
)

class PersonForm(forms.Form):
    name = forms.CharField(
        label = 'Your Name', 
        label_suffix = "  ", 
        help_text = "name field enter your full name.", 
        required = False,
        disabled = True,
        widget = forms.TextInput(attrs = {'class': 'some_css', 'id': 'unique_id'})
    )
    email = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput)
    age = forms.IntegerField(initial = 24)
    first_name = forms.CharField(
        initial = "Ganesh", 
        min_length = 5, 
        max_length = 10, 
        strip = False,
        empty_value = "Kartikay",
        error_messages = {'required': "Deepraj this field is required", 'min_length': "Bro write at least 5 characters"}
    )
    # underscore will be convert to space charachter while showing in form 
    key = forms.CharField(widget = forms.HiddenInput(), initial = 15, required = False)
    address = forms.CharField(widget = forms.Textarea, required = False)
    policy = forms.CharField(widget = forms.CheckboxInput, required = False, initial = "accepted")
    image = forms.CharField(widget = forms.FileInput, required = False)
    roll_number = forms.IntegerField(min_value = 5, max_value = 10)
    price = forms.DecimalField(min_value = 5, max_value = 40, max_digits = 4, decimal_places = 1)
    rate = forms.FloatField(min_value = 5, max_value = 40)
    choose_number = forms.ChoiceField(choices = GEEKS_CHOICES)
    agree = forms.BooleanField(label = "I agree", label_suffix = "")

class StudentForm(forms.Form):
    student_name = forms.CharField()
    student_email = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput)
    roll_number = forms.IntegerField(min_value = 1, max_value = 1000)

    # def clean_name(self):
    #     """
    #         Validate one form field
    #     """
    #     value_of_student_name = self.cleaned_data["student_name"]
    #     if len(value_of_student_name) < 4:
    #         raise forms.ValidationError("Your name should be more than 4 characters.")
    #     return value_of_student_name

    def clean(self):
        """
            Validate all form fields
        """
        cleaned_data = super().clean()
        value_of_student_name = ""
        if "student_name" in self.cleaned_data:
            value_of_student_name = self.cleaned_data["student_name"]
        value_of_student_email = ""
        if "student_email" in self.cleaned_data:
            value_of_student_email = self.cleaned_data['student_email']
        if len(value_of_student_name) < 4:
            raise forms.ValidationError("Your name should be more than 4 characters in whole validation.")
        if len(value_of_student_email) < 10:
            raise forms.ValidationError(["Your email should be more than 10 characters in whole validation.", "second"])
        # raise forms.ValidationError({"student_name": [], "student_email": ["first one", "second one"], "password": "third one"})

def starts_with_s(value):
    if value[0] != 's':
        raise forms.ValidationError("Name should start with s")

class TeacherForm(forms.Form):
    # for showing error classes in trs of that specific fields
    error_css_class = "error_class"
    required_css_class = "required_error_class"
    teacher_name = forms.CharField(validators=[validators.MaxLengthValidator(10), starts_with_s])
    teacher_email = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput)
    confirm_password = forms.CharField(widget = forms.PasswordInput)
    roll_number = forms.IntegerField(min_value = 1, max_value = 1000)

    def clean(self):
        """
            Validate all form fields
        """
        cleaned_data = super().clean()
        value_of_password = ""
        if "password" in self.cleaned_data:
            value_of_password = self.cleaned_data["password"]
        value_of_confirm_password = ""
        if "confirm_password" in self.cleaned_data:
            value_of_confirm_password = self.cleaned_data['confirm_password']
        if value_of_password != value_of_confirm_password:
            raise forms.ValidationError({"confirm_password": "Your password and confirm password are not matched."})

class StudentModelForm(forms.ModelForm):
    roll_number = forms.IntegerField(min_value = 1, max_value = 1000)
    class Meta:
        model = Student
        fields = ['roll_number', 'student_name', 'student_email', 'password']
        labels = {"roll_number" : "Enter Roll Number", "password": "PAssword", "student_email": "Student Email :- ", "student_name": "Student Name      "}
        help_text = {"roll_number" : "Roll Number Help", "password": "PAssword HElp", "student_email": "Student Email :- Help", "student_name": "Student Name      Help"}
        widgets = {'password': forms.PasswordInput}
        error_messages = {"roll_number" : {"required": "You have to add roll number it is required"}, 
            "password": {"required": "You have to enter password it is required"}, 
            "student_email": {"required": "You have to enter email it is required"}, 
            "student_name": {"required": "You have to enter name it is required"}}
    
    def clean(self):
        """
            Validate all form fields
        """
        cleaned_data = super().clean()
        value_of_student_name = ""
        if "student_name" in self.cleaned_data:
            value_of_student_name = self.cleaned_data["student_name"]
        value_of_student_email = ""
        if "student_email" in self.cleaned_data:
            value_of_student_email = self.cleaned_data['student_email']
        if len(value_of_student_name) < 4:
            raise forms.ValidationError("Your name should be more than 4 characters in whole validation.")
        if len(value_of_student_email) < 10:
            raise forms.ValidationError(["Your email should be more than 10 characters in whole validation.", "second"])
        # raise forms.ValidationError({"student_name": [], "student_email": ["first one", "second one"], "password": "third one"})

class TeacherModelForm(forms.ModelForm):
    error_css_class = "error_class"
    required_css_class = "required_error_class"
    teacher_name = forms.CharField(validators=[validators.MaxLengthValidator(10), starts_with_s])
    confirm_password = forms.CharField(widget = forms.PasswordInput)
    roll_number = forms.IntegerField(min_value = 1, max_value = 1000)

    class Meta:
        model = Teacher
        fields = ['roll_number', 'teacher_name', 'teacher_email', 'password']
        widgets = {'password': forms.PasswordInput}
    
    def clean(self):
        """
            Validate all form fields
        """
        cleaned_data = super().clean()
        value_of_password = ""
        if "password" in self.cleaned_data:
            value_of_password = self.cleaned_data["password"]
        value_of_confirm_password = ""
        if "confirm_password" in self.cleaned_data:
            value_of_confirm_password = self.cleaned_data['confirm_password']
        if value_of_password != value_of_confirm_password:
            raise forms.ValidationError({"confirm_password": "Your password and confirm password are not matched."})
        