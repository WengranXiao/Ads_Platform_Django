from django.contrib import admin

from movies.models import Movie, Genre

admin.site.register(Genre)
admin.site.register(Movie)

