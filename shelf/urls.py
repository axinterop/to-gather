from django.urls import path

from . import views

app_name = "shelf"
urlpatterns = [
    path("", views.index, name="index"),
    path("movies/all/", views.movie_list_all, name="movie_list_all"),
    path("movies/add/", views.movie_add, name="movie_add")
]