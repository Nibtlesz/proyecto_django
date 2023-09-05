from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def welcome(request):
    return render(request, 'website/welcome.html', {
        "info": "Curso Introductorio de Django", 
        "suma": 5+2
    
    })

def date(request):
    return HttpResponse("la hora en servidor es: " + str(datetime.now()))

def page_not_found(request, exception):
    return render(request, 'website/404.html', status=404)