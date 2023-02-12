from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.db.models import F, Sum, Max, Min, Count, Avg


def show_all_movies(request):
    movies = Movie.objects.order_by(F('year').desc(nulls_last=True), 'rating')
    aggregate = movies.aggregate(Sum('budget'), Avg('budget'), Avg('rating'), Min('rating'), Max('rating'), Count('id'))
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'aggregate': aggregate
    })


# def show_one_movie(request, id_movie:int):
#     # movie = Movie.objects.get(id=id_movie)
#     movie = get_object_or_404(Movie, id=id_movie)
#     return render(request, 'movie_app/one_movie.html', {
#         'movie': movie
#     })

def show_one_movie(request, slug_movie: str):
    # movie = Movie.objects.get(id=id_movie)
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })
