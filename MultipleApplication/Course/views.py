from django.shortcuts import render
from django.http import HttpResponse 

def django(request):
    return render(request, 'course/django.html')

def node(request):
    return render(request, 'course/node.html')

def unknownCourse(request, *args, **kwargs):
    if("unknown" in kwargs):
        return render(request, 'course/unknown.html', kwargs)
    return render(request, 'core/unknown.html')    