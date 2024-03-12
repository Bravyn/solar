from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from .models import StarDetails

# Create your views here.
def star(request: HttpRequest ):
    template = loader.get_template("stars.html")
    return HttpResponse(template.render())

def about(request: HttpRequest ):
    template2 = loader.get_template("about.html")
    return HttpResponse(template2.render())
    
def home(request: HttpRequest):
    stars = StarDetails.objects.all().values()
    home_template = loader.get_template("home.html")
    context = {
        'stars': stars
    }
    return HttpResponse(home_template.render(context))

def star_details(request):
    star = StarDetails.objects.all().values()
    template = loader.get_template('star_details.html')
    context = {
        'star': star,
    }
    return HttpResponse(template.render(context))

