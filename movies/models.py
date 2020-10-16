from django.db import models
from .utils import generate_genre_id, generate_movie_id


class Genre(models.Model):
    _id = models.CharField(primary_key=True, max_length=100, blank=True)
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self._id = generate_genre_id()
        super(Genre, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Movie(models.Model):
    _id = models.CharField(primary_key=True, max_length=100, blank=True)
    title = models.CharField(max_length=100)
    numberInStock = models.IntegerField(default=0)
    dailyRentalRate = models.DecimalField(default=0.0, decimal_places=2, max_digits=10)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='genre')
    liked = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self._id:
            self._id = generate_movie_id()
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.title