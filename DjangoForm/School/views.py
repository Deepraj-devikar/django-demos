from django.shortcuts import render
from .forms import *

def person_form(request, *args, **kwargs):
    data = {}
    data["personForm"] = PersonForm(
        auto_id = "some_%s", 
        label_suffix = " Some :-  ",
        initial={"name": "Ganesh"}
    )
    #-----------------auto_id-----------------
    # auto_id by default 'id_%s',
    # if we make auto_id = True or any other value which dont have %s like 'some' then it will be '%s'
    # if we make auto_id = False then it wiil not show id it will be ''
    #-----------------label_suffix---------------
    # label_sufix by default ':' we can change it by providing string
    #-----------------intial---------------------
    # for setting initial values of fields
    # we can use it in edit page
    return render(request, "School/person_form.html", data)
    