"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/mmm/',views.MovieListAPIView.as_view()),
    path('api/v1/directors/',views.DirectorListAPIView.as_view()),
    path('api/v1/directors/<int:id>/',views.DirectorUpdateDeleteAPIView.as_view()),
    path('api/v1/movie/',views.MovieListAPIView.as_view()),
    path('api/v1/movie/<int:id>/',views.MovieUpdateDeleteAPIView.as_view()),
    path('api/v1/review/',views.ReviewListAPIView.as_view()),
    path('api/v1/review/<int:id>/',views.RetrieveUpdateDestroyAPIView.as_view()),
    path('api/v1/movie/review/',views.RetrieveUpdateDestroyAPIView.as_view()),
    path('api/v1/login/',views.AuthorizationAPIView.as_view()),
    path('api/v1/register/',views.RegisterAPIView.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]
