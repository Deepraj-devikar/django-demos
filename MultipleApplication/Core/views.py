from django.shortcuts import render

def unknown(request, *args, **kwargs):
    return render(request, 'core/unknown.html')