from django.http import HttpResponse 

def helloWorld(request):
    return HttpResponse("<h1>Hello World</h1>")

def helloView(request):
    return HttpResponse("<h1>Hello View</h1>")