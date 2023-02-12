from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', 'budget']
    list_editable = ['rating', 'year', 'budget']
    ordering = ['rating']
    list_per_page = 3


# admin.site.register(Movie, MovieAdmin)
