from django.shortcuts import render

def django(request, *args, **kwargs):
    return render(request, 'fees_django.html')
    

def node(request, *args, **kwargs):
    return render(request, 'fees_node.html')

def unknown(request, *args, **kwargs):
    return render(request, 'fees_unknown.html', kwargs)