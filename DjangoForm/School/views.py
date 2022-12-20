from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *

def person_form(request, *args, **kwargs):
    data = {}
    if request.method == 'POST':
        personForm = PersonForm(request.POST)
        if personForm.is_valid():
            print("Form Validated")
            for formField, formFieldValue in personForm.cleaned_data.items():
                print(formField+" => "+str(formFieldValue))
            url = reverse("person_info")
            return HttpResponseRedirect(url)             
            # return render(request, "School/person_info.html", data)
    else:
        personForm = PersonForm(
            auto_id = "some_%s", 
            label_suffix = " Some :-  ",
            initial={"name": "Ganesh", "age": 20}
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
    personForm.order_fields(["name", "first_name"])
    # we can set fields order
    # if some fields not included in order_fields then that remaining feilds will follow default order after mentioned fields
    data["personForm"] = personForm
    return render(request, "School/person_form.html", data)

def person_info(request, *args, **kwargs):
    return render(request, "School/person_info.html", {})

    