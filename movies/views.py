from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})
    # output = ", ".join([m.title for m in moives])
    # return HttpResponse(output)


def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
