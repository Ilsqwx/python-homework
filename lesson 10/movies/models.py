from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    poster = models.ImageField(upload_to='posters/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title