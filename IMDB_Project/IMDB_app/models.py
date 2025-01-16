from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class StreamPlatforms(models.Model):
    name=models.CharField(max_length=30)
    about = models.CharField(max_length=150, blank=True)
    website = models.URLField(max_length=100)
    
    def __str__(self):
        return self.name

class WatchList(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField(max_length=150, blank=True)
    platform = models.ForeignKey(StreamPlatforms, on_delete=models.CASCADE, related_name="channel")
    avg_reviews = models.FloatField(default=0)
    number_reviews = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Review(models.Model):
    Review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(max_length=150, blank=True)
    active=models.BooleanField(default=True)
    movielist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="movies")
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.rating) + "/" + self.movielist.title