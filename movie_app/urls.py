from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.show_all_movies),
]