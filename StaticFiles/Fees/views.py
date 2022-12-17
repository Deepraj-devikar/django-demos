from django.shortcuts import render

def django(request, *args, **kwargs):
    return render(request, "fees/django.html", {})
    
def node(request, *args, **kwargs):
    return render(request, "fees/node.html", {})

def unknown(request, *args, **kwargs):
    return render(request, "fees/unknown.html", kwargs)
       