from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


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
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1)])
    currency = models.CharField(max_length=6, choices=MONEY_CURRENCY_CHOICES, default=SOM)
    budget = models.IntegerField(default=1000000)
    slug = models.SlugField(default='', null=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('movie-detail', args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.rating}%'
