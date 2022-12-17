from django.shortcuts import render

def allCourses(request, *args, **kwargs):
    print("getting")
    return render(request, "course/all_courses.html")

def django(request, *args, **kwargs):
    return render(request, "course/django.html")

def node(request, *args, **kwargs):
    return render(request, "course/node.html")
        
    