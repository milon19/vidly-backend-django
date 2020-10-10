from rest_framework import serializers

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
    genre = GenreSerializer(read_only=True)

    class Meta:
        model = Movie
        fields = ('_id', 'title', 'numberInStock', 'dailyRentalRate', 'liked', 'genre')
        extra_kwargs = {
            '_id': {
                'read_only': True,
            },
        }
