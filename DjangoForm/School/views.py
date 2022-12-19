from django.shortcuts import render
from .forms import *

def person_form(request, *args, **kwargs):
    data = {}
    data["personForm"] = PersonForm()
    return render(request, "School/person_form.html", data)
    