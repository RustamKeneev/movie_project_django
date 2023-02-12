from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.show_all_movies),
    path('movie/<int:id_movie>', views.show_one_movie, name='movie-detail'),
]