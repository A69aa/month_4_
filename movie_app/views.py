from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializers import DirectorSerializers, ReviewSerializers, MovieSerializers
from movie_app.models import Movie, Director,Review
from rest_framework import status
from . import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from .serializers import UserCreateSerializer,UserAuthorizationSerializer


class DirectorListAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializers


class DirectorUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializers
    lookup_field = 'id'

#
# @api_view(['GET','POST'])
# def director_list_view(request):
#     if request.method == 'GET':
#         director = Director.objects.all()
#         data = DirectorSerializers(director, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = serializers.DirectorCreateUpdateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(data={'error':serializer.errors},status=status.HTTP_406_NOT_ACCEPTABLE)
#         else:
#             name = request.data.get('name')
#             director = Director.objects.create(name=name)
#             return Response(data=DirectorSerializers(director).data,
#                             status=status.HTTP_201_CREATED)
#
# @api_view(['GET','PUT','DELETE'])
# def director_detail_view(request, id):
#     try:
#         director = Director.objects.get(id=id)
#     except Director.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND,
#                         data={'message':'Режиссер по вашему запросу не найден!'})
#     if request.method == 'GET':
#         data = DirectorSerializers(director).data
#         return Response(data=data)
#     elif request.method == 'PUT':
#         serializer = serializers.DirectorCreateUpdateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(data={'error':serializer.errors},status=status.HTTP_406_NOT_ACCEPTABLE)
#         else:
#             director.name = request.data.get('name')
#             director.save()
#             return Response(data=DirectorSerializers(director).data)
#     elif request.method == 'DELETE':
#         director.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class MovieListAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers


class MovieUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    lookup_field = 'id'

#
#
# @api_view(['GET','POST'])
# def movie_list_view(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         data = MovieSerializers(movies,many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = serializers.MovieCreateUpdateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(data={'error':serializer.errors},status=status.HTTP_406_NOT_ACCEPTABLE)
#         else:
#             title = request.data.get('title')
#             description = request.data.get('description')
#             duration = request.data.get('duration')
#             director = request.data.get('director')
#             movies = Movie.objects.create(title=title,description=description,
#                                    duration=duration,director_id=director)
#             return Response(data=MovieSerializers(movies).data,
#                             status=status.HTTP_201_CREATED)
#
# @api_view(['GET','PUT','DELETE'])
# def movie_detail_view(request,id):
#     try:
#         movie = Movie.objects.get(id=id)
#     except Movie.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND,
#                         data={'message':'Фильм по вашему запросу не найден!'})
#     if request.method == 'GET':
#         data = MovieSerializers(movie).data
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         serializer = serializers.MovieCreateUpdateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(data={'error':serializer.errors},status=status.HTTP_406_NOT_ACCEPTABLE)
#         else:
#             movie.title = request.data.get('title')
#             movie.description = request.data.get('description')
#             movie.duration = request.data.get('duration')
#             movie.director_id =  request.data.get('director')
#             movie.save()
#             return Response(data=MovieSerializers(movie).data)

class ReviewListAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers


class ReviewUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    lookup_field = 'id'


#
# @api_view(['GET','POST'])
# def review_list_view(request):
#     if request.method == 'GET':
#         reviews = Review.objects.all()
#         data = ReviewSerializers(reviews,many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = serializers.ReviewCreateUpdateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(data={'error':serializer.errors},status=status.HTTP_406_NOT_ACCEPTABLE)
#         else:
#             text = request.data.get('text')
#             movie_id = request.data.get('movie_id')
#             stars = request.data.get('stars')
#             reviews = Review.objects.create(text=text,movie_id=movie_id,stars=stars)
#             return Response(data=ReviewSerializers(reviews).data,
#                             status=status.HTTP_201_CREATED)
#
# @api_view(['GET','PUT','DELETE'])
# def review_detail_view(request,id):
#     try:
#         reviews = Review.objects.get(id=id)
#     except Review.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND,
#                         data={'message':'Отзыв по вашему запросу не найден!'})
#     if request.method == 'GET':
#         data = ReviewSerializers(reviews).data
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         reviews.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         serializer = serializers.ReviewCreateUpdateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(data={'error':serializer.errors},status=status.HTTP_406_NOT_ACCEPTABLE)
#         else:
#             reviews.text = request.data.get('text')
#             reviews.movie = request.data.get('movie')
#             reviews.stars = request.data.get('stars')
#             reviews.movie_id = request.data.get('movie_id')
#             reviews.save()
#             return Response(data=ReviewSerializers(reviews).data)


class AuthorizationAPIView(APIView):
    serializer_class = UserAuthorizationSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.authenticate(**serializer.validated_data)
        return Response(data={'error': 'User not found'},
                        status=status.HTTP_404_NOT_FOUND)
#
# @api_view(['POST'])
# def authorization(request):
#     if request.method == 'POST':
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username,password=password)
#         if user:
#             try:
#                 token = Token.objects.get(user=user)
#             except Token.DoesNotExist:
#                 token = Token.objects.create(user=user)
#                 return Response(data={'key':token.key})
#
#         return Response(data={'error':'User not found'},
#                         status=status.HTTP_404_NOT_FOUND)
#

class RegisterAPIView(APIView):
    serializer_class = UserCreateSerializer
    def post(self,request):
        serializers = self.serializer_class(data=request.data)
        serializers.is_valid(raise_exception=True)
        User.objects.create_user(**serializers.validated_data)
        return Response(data={'message':'Пользователь Создан!'},
                        status=status.HTTP_201_CREATED)
#
# @api_view(['POST'])
# def registration(request):
#     if request.method == 'POST':
#         username = request.data.get('username')
#         password = request.data.get('password')
#         User.objects.create_user(username=username,password=password)
#         return Response(data={'message':'User created'},
#                         status=status.HTTP_201_CREATED)
#

