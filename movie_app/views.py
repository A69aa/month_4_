from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializers import DirectorSerializers, ReviewSerializers, MovieSerializers
from movie_app.models import Movie, Director,Review
from rest_framework import status



@api_view(['GET'])
def director_list_view(request):
    director = Director.objects.all()
    data = DirectorSerializers(director, many=True).data
    return Response(data=data)

@api_view(['GET'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message':'Режиссер по вашему запросу не найден!'})
    data = DirectorSerializers(director).data
    return Response(data=data)




@api_view(['GET'])
def movie_list_view(request):
    movies = Movie.objects.all()
    data = MovieSerializers(movies,many=True).data
    return Response(data=data)


@api_view(['GET'])
def movie_detail_view(request,id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message':'Фильм по вашему запросу не найден!'})
    data = MovieSerializers(movie).data
    return Response(data=data)



@api_view(['GET'])
def review_list_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializers(reviews,many=True).data
    return Response(data=data)


@api_view(['GET'])
def review_detail_view(request,id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message':'Отзыв по вашему запросу не найден!'})
    data = ReviewSerializers(reviews).data
    return Response(data=data)






