from django.shortcuts import render

def django(request, *args, **kwargs):
    return render(request, "course/django.html", {})
    
def node(request, *args, **kwargs):
    return render(request, "course/node.html", {})

def unknown(request, *args, **kwargs):
    return render(request, "course/unknown.html", kwargs)
       