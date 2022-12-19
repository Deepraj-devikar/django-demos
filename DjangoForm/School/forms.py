from django import forms 

class PersonForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    age = forms.IntegerField()
    first_name = forms.CharField()
    # underscore will be convert to space charachter while showing in form 
    