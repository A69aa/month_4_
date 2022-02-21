from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def count_movies(self):
        return self.movies.all().count()


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    duration = models.IntegerField()
    director = models.ForeignKey(Director,on_delete=models.CASCADE)
    # review = models.ForeignKey(Review,on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Review(models.Model):
    text = models.TextField(null=True,blank=True)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField(default=0,validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],null=True)

    def __str__(self):
        return self.text

    @property
    def rating(self):
        reviews = Review.objects.filter(text=self)
        sum_ = 0
        for i in reviews:
            sum_ += i.stars
        return sum_ / reviews.count()


