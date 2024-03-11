from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader

# Create your views here.
def star(request: HttpRequest ):
    template = loader.get_template("stars.html")
    return HttpResponse(template.render())

def about(request: HttpRequest ):
    template2 = loader.get_template("about.html")
    return HttpResponse(template2.render())
    
def home(request):
    home_template = loader.get_template("home.html")
    return HttpResponse(home_template.render())