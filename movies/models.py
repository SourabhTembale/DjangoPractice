from django.db import models

# Create your models here.
class Movie(models.Model):
    Series_Title = models.CharField(max_length=225)
    Released_year = models.IntegerField()
    Genre = models.CharField(max_length=225)
    IMDB_rating = models.FloatField()

    def __str__(self):
        return self.title