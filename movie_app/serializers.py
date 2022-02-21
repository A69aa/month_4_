from rest_framework import serializers
from movie_app.models import Director, Review,Movie


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name count_movies'.split()

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text movie stars rating'.split()

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'title description duration director'.split()

