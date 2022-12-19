from django import forms 

class PersonForm(forms.Form):
    name = forms.CharField(help_text = "name field enter your full name.")
    email = forms.EmailField()
    age = forms.IntegerField(initial = 24)
    first_name = forms.CharField(initial = "Ganesh")
    # underscore will be convert to space charachter while showing in form 
    