from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from movies.models import Movie, Genre
from movies.forms import GenreForm

class MovieList (LoginRequiredMixin, View) :
    def get(self, request):
        mc = Genre.objects.all ().count ();
        al = Movie.objects.all ();
        ctx = { 'genre_count': mc, 'movie_list': al };
        return render(request, 'movies/movie_list.html', ctx)
class GenreView (LoginRequiredMixin,View) :
    def get (self, request):
        ml = Genre.objects.all ();
        ctx = { 'genre_list': ml };
        return render(request, 'movies/genre_list.html', ctx)

class GenreCreate (LoginRequiredMixin, CreateView):
    model = Genre
    fields = '__all__'
    success_url = reverse_lazy('movies:all')
class GenreUpdate (LoginRequiredMixin, UpdateView):
    model = Genre
    fields = '__all__'
    success_url = reverse_lazy('movies:all')
class GenreDelete(LoginRequiredMixin, DeleteView):
    model = Genre
    fields = '__all__'
    success_url = reverse_lazy('movies:all')

class MovieCreate(LoginRequiredMixin, CreateView):
    model = Movie
    fields = '__all__'
    success_url = reverse_lazy('movies:all')


class MovieUpdate(LoginRequiredMixin, UpdateView):
    model = Movie
    fields = '__all__'
    success_url = reverse_lazy('movies:all')


class MovieDelete(LoginRequiredMixin, DeleteView):
    model = Movie
    fields = '__all__'
    success_url = reverse_lazy('movies:all')
