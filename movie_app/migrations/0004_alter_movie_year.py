# Generated by Django 4.1.6 on 2023-02-12 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_movie_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
