from django.shortcuts import render

def welcome(request, *args, **kwargs):
    return render(request, "createurl/welcome.html", kwargs)

def welcome_to_home(request, *args, **kwargs):
    return render(request, "createurl/welcome_to_home.html", kwargs)

def show_details(request, my_id="1", **check):
    print(my_id)
    if my_id == "1":
        student = {"id": my_id, "name": "Rajesh"}
    elif my_id == "2":
        student = {"id": my_id, "name": "Suresh"}
    else:
        student = {"id": my_id, "name": "Prakash"}
    print(check)
    return render(request, "createurl/show.html", student)

def show_subdetails(request, my_id, my_subid, **check):
    print(my_id)
    if my_id == "1" and my_subid == "5":
        student = {"id": my_id, "name": "Rajesh", "info": "sub details"}
    elif my_id == "2" and my_subid == "6":
        student = {"id": my_id, "name": "Suresh", "info": "sub details"}
    else:
        student = {"id": my_id, "name": "Prakash", "info": "sub details"}
    return render(request, "createurl/show.html", student)
    
def home(request):
    return render(request, "createurl/home.html")
    
def show_year(request, year):
    return render(request, "createurl/show_year.html", {"year": year})
    