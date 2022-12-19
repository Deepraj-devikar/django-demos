from django.shortcuts import render
from .forms import *

def person_form(request, *args, **kwargs):
    data = {}
    data["personForm"] = PersonForm(auto_id = "")
    # auto id by default 'id_%s',
    # if we make auto_id = True or any other value which dont have %s like 'some' then it will be '%s'
    # if we make auto_id = False then it wiil not show id it will be ''
    return render(request, "School/person_form.html", data)
    