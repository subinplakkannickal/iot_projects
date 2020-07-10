from django.db import models

# Create your models here.

class Movie(object):
    id : int
    name : str
    language : str
    category : str


class Music(object):
    id : int
    name : str
    language : str
    category : str