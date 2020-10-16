from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from .models import Movie, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('_id', 'name')
        extra_kwargs = {
            '_id': {
                'read_only': True,
            },
        }


class MovieSerializer(serializers.ModelSerializer):
    genre_obj = GenreSerializer(source='genre', read_only=True)
    # genre = PrimaryKeyRelatedField(queryset=Genre.objects.all(), write_only=True)

    class Meta:
        model = Movie
        fields = ('_id', 'title', 'numberInStock', 'dailyRentalRate', 'genre', 'liked', 'genre_obj')
        extra_kwargs = {
            '_id': {
                'read_only': True,
            },
        }
