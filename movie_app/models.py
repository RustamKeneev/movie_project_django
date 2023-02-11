from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.rating}%'