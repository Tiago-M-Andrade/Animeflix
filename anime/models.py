from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

CATEGORY_LIST = (
    ("DRAMA", "Drama"),
    ("SUPERNATURAL", "Supernatural"),
    ("HORROR", "Horror"),
    ("MYSTERY", "Mystery"),
    ("COMEDY", "Comedy"),
    ("ROMANCE", "Romance"),
    ("ACTION", "Action"),
    ("FANTASY", "Fantasy"),
    ("ECCHI", "Ecchi"),
    ("ADVENTURE", "Adventure")
)

# Create your models here.  
class Anime(models.Model):
    title = models.CharField(max_length=150)
    thumb = models.ImageField(upload_to='thumb_animes')
    description = models.TextField(max_length=1000)
    num_views = models.IntegerField(default=0)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
class Episode(models.Model):
    anime = models.ForeignKey("Anime", related_name="episodes", on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    video2 = models.FileField(upload_to="video/%y")
    thumb = models.FileField(upload_to="thumb/%y",blank=True)

    def __str__(self):
        return self.anime.title + " - " + self.title
    
class Categorie(models.Model):
    name = models.ForeignKey(Anime, related_name='category', blank=True, null=True, on_delete=models.DO_NOTHING)
    category = models.CharField(max_length=18, choices=CATEGORY_LIST)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name.title + " - " + self.category
    
class User(AbstractUser):
    watched_movies = models.ManyToManyField("Anime")
    user_image = models.ImageField(upload_to='profile_img', blank=True)