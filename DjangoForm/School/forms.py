from django import forms 

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