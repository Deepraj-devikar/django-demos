from django import forms 

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
    first_name = forms.CharField(initial = "Ganesh")
    # underscore will be convert to space charachter while showing in form 
    key = forms.CharField(widget = forms.HiddenInput(), initial = 15, required = False)
    address = forms.CharField(widget = forms.Textarea, required = False)
    policy = forms.CharField(widget = forms.CheckboxInput, required = False, initial = "accepted")
    image = forms.CharField(widget = forms.FileInput, required = False)