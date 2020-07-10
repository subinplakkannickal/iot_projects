from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="ms_index"),
    path('movies', views.movies, name="ms_movies"),
    path('musics', views.musics, name="ms_musics"),
    path('about', views.about, name="ms_about"),
    path('contact', views.contact, name="ms_contact"),
    path('signup', views.signup, name="ms_signup"),
    path('signin', views.signin, name="ms_signin"),
    path('test', views.test, name="ms_test"),
]
