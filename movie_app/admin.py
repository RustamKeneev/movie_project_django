from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'currency', 'budget', 'rating_status']
    list_editable = ['rating', 'currency', 'budget']
    ordering = ['rating']
    list_per_page = 3

    @admin.display(ordering='rating', description='Статус фильмов')
    def rating_status(self, movie: Movie):
        if movie.rating < 50:
            return "Рейтинг менее 50 процентов не рекомендую"
        if movie.rating < 70:
            return "Рейтинг менее 70 процентов можно рекомендовать"
        if movie.rating <= 85:
            return "Рейтинг менее 85 процентов  рекомендую"
        return 'Рекомендованные'

# admin.site.register(Movie, MovieAdmin)
