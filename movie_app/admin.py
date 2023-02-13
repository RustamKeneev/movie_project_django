from django.contrib import admin, messages
from .models import Movie
from django.db.models import QuerySet


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'currency', 'budget', 'rating_status']
    list_editable = ['rating', 'currency', 'budget']
    ordering = ['rating']
    list_per_page = 3
    actions = ['set_dollars', 'set_som']
    search_fields = ['name', 'rating']

    @admin.display(ordering='rating', description='Статус фильмов')
    def rating_status(self, movie: Movie):
        if movie.rating < 50:
            return "Рейтинг менее 50 процентов не рекомендую"
        if movie.rating < 70:
            return "Рейтинг менее 70 процентов можно рекомендовать"
        if movie.rating <= 85:
            return "Рейтинг менее 85 процентов  рекомендую"
        return 'Рекомендованные'

    @admin.action(description="Установить валюту в доллар")
    def set_dollars(self, request, queryset_data: QuerySet):
        queryset_data.update(currency=Movie.DOL)

    @admin.action(description="Установить валюту в сом")
    def set_som(self, request, queryset_data: QuerySet):
        count_update = queryset_data.update(currency=Movie.SOM)
        self.message_user(
            request,
            f'Было обновлено {count_update} записей',
            messages.ERROR
        )

# admin.site.register(Movie, MovieAdmin)
