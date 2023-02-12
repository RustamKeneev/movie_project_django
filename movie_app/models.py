from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Movie(models.Model):
    SOM = 'SOM'
    EU = "Euro"
    DOL = "Dollar"
    RUB = "Rubles"
    MONEY_CURRENCY_CHOICES = [
        (SOM, "Som"),
        (EU, "Euro"),
        (DOL, "Dollar"),
        (RUB, "Rubles"),
    ]
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=6, choices=MONEY_CURRENCY_CHOICES, default=SOM)
    budget = models.IntegerField(default=1000000)
    slug = models.SlugField(default='', null=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    #
    # def get_url(self):
    #     return reverse('movie-detail', args=[self.id])

    def get_url(self):
        return reverse('movie-detail', args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.rating}%'
