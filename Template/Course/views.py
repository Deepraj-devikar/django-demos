from django.shortcuts import render

def django(request, *args, **kwargs):
    return render(request, 'course_django.html')
    

def node(request, *args, **kwargs):
    return render(request, 'course_node.html')

def unknown(request, *args, **kwargs):
    return render(request, 'course_unknown.html', kwargs)