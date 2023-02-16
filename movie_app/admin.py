from django.contrib import admin, messages
from .models import Movie, Director, Actor, DressingRoom
from django.db.models import QuerySet


admin.site.register(Director)
admin.site.register(Actor)
# admin.site.register(DressingRoom)


@admin.register(DressingRoom)
class DressingRoomAdmin(admin.ModelAdmin):
    list_display = ['floor', 'number', 'actor']


class RatingFilter(admin.SimpleListFilter):
    title = "Фильтр по рейтингу"
    parameter_name = "rating"

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий'),
            ('от 40 до 59', 'Средний'),
            ('от 60 до 89', 'Высокий'),
            ('>=90', 'Высочящий'),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == "<40":
            return queryset.filter(rating__lt=40)
        if self.value() == "от 40 до 59":
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        if self.value() == "от 60 до 89":
            return queryset.filter(rating__gte=60).filter(rating__lt=89)
        if self.value() == ">=90":
            return queryset.filter(rating__gte=90)
        return queryset


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # exclude = ['slug']
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'rating', 'director', 'budget', 'rating_status']
    list_editable = ['rating', 'director', 'budget']
    ordering = ['rating']
    list_per_page = 3
    actions = ['set_dollars', 'set_som']
    search_fields = ['name', 'rating']
    list_filter = ['name', 'currency', RatingFilter]
    filter_horizontal = ['actors']

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
