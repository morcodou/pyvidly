from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie
# Create your views here.


def index(request):
    moives = Movie.objects.all()
    output = ", ".join([m.title for m in moives])
    return HttpResponse(output)
