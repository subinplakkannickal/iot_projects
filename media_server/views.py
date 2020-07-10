from django.shortcuts import render
from django.http import HttpResponse

from media_server.models import Movie, Music


# Create your views here.

def index(request):
    return render(request, 'ms_index.html')

def movies(request):
    movie_1 = Movie()
    movie_1.id = 1
    movie_1.name = 'Like a butterfly'
    movie_1.language = 'English'
    movie_1.category = 'Action'

    movie_2 = Movie()
    movie_2.id = 2
    movie_2.name = 'Mind & Body'
    movie_2.language = 'English'
    movie_2.category = 'Romantic'

    movie_3 = Movie()
    movie_3.id = 3
    movie_3.name = 'Crit Cardio'
    movie_3.language = 'Malayalam'
    movie_3.category = 'Thriller'
    
    movie_4 = Movie()
    movie_4.id = 4
    movie_4.name = 'Wheel Pose Full Posture'
    movie_4.language = 'Hindi'
    movie_4.category = 'Action'
    
    return render(request, 'ms_movies.html', {'movie_items' : [movie_1, movie_2, movie_3, movie_4, movie_4, movie_4, movie_4]})

def musics(request):
    music_1 = Music()
    music_1.id = 1
    music_1.name = 'Like a butterfly'
    music_1.language = 'English'
    music_1.category = 'Action'

    music_2 = Music()
    music_2.id = 2
    music_2.name = 'Mind & Body'
    music_2.language = 'English'
    music_2.category = 'Romantic'

    music_3 = Music()
    music_3.id = 3
    music_3.name = 'Crit Cardio'
    music_3.language = 'Malayalam'
    music_3.category = 'Thriller'
    
    music_4 = Music()
    music_4.id = 4
    music_4.name = 'Wheel Pose Full Posture'
    music_4.language = 'Hindi'
    music_4.category = 'Action'
    return render(request, 'ms_musics.html', {'music_items' : [music_1, music_2, music_3, music_4, music_4, music_4, music_4]})

def about(request):
    return render(request, 'ms_about.html')

def contact(request):
    return render(request, 'ms_contact.html')

def signup(request):
    print (request)
    return render(request, 'ms_signup.html')

def signin(request):
    return render(request, 'ms_signin.html')

def test(request):
    email = request.POST['email']
    pawwsord = request.POST['password']
    return render(request, 'ms_signin.html')
