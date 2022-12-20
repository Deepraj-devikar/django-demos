from django import forms 

class PersonForm(forms.Form):
    name = forms.CharField(
        label = 'Your Name', 
        label_suffix = "  ", 
        help_text = "name field enter your full name.", 
        required = False,
        disabled = True
    )
    email = forms.EmailField()
    age = forms.IntegerField(initial = 24)
    first_name = forms.CharField(initial = "Ganesh")
    # underscore will be convert to space charachter while showing in form 
    key = forms.CharField(widget = forms.HiddenInput())