from django.shortcuts import render

def django(request):
    return render(request, 'fees/django.html')

def node(request):
    return render(request, 'fees/node.html')

def unknownFees(request, *args, **kwargs):
    if("unknown" in kwargs and "fees" in kwargs):
        return render(request, 'fees/unknown.html', kwargs)
    return render(request, 'core/unknown.html')