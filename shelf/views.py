from django.shortcuts import render, redirect, reverse, HttpResponse
from .models import Movie
from .forms import MovieForm

def index(request):
    return render(request, "shelf/index.html")


def movie_list_all(request):
    movies = Movie.objects.all()
    context = {
        "movies": movies,
    }
    return render(request, "shelf/movie_list_all.html", context)

def movie_add(request):
    if request.method == "POST":
        f = MovieForm(request.POST)
        new_movie = f.save()
        return redirect(reverse("shelf:movie_list_all"))
    else:
        form = MovieForm()
        context = {
            "form": form
        }
    return render(request, "shelf/movie_add.html", context)