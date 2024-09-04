from django.db import models
from django.conf import settings

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movie')
    title = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre)
    movie_id = models.IntegerField()
    overview = models.TextField()
    popularity = models.IntegerField()
    poster_path = models.CharField(max_length=200)
    release_date = models.DateField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    backdrop_path = models.CharField(max_length=200)

class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews', blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')