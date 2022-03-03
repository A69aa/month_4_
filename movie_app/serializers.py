from rest_framework import serializers
from movie_app.models import Director, Review,Movie
from rest_framework.serializers import SerializerMethodField
from . import models
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'
        # fields = 'name count_movies'.split()

class DirectorCreateUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)




class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text movie stars rating'.split()

class ReviewCreateUpdateSerializer(serializers.Serializer):
    text = serializers.CharField()
    movie_id = serializers.IntegerField()
    stars = serializers.IntegerField(min_value=1, max_value=5)

    def validate_movie_id(self, movie_id):
        if models.Movie.objects.filter(id=movie_id).count==0:
            raise ValidationError(f'message: movie id not found')




class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description duration director'.split()

class MovieCreateUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    duration = serializers.IntegerField()
    director_id = serializers.IntegerField()

    def validate_director_id(self, attrs):
        if models.Director.objects.filter(id=attrs).count==0:
            raise ValidationError(f'message:{attrs} not found')


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


    def validate_username(self,username):
        if User.objects.filter(username=username):
            raise ValidationError('user with this username is already exists')
        return username


class UserAuthorizationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_token(self,token):
        if User.objects.filter(token=token):
            raise ValidationError('this user is already logged in')

