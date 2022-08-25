from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

from django.forms import URLField
from django.core.validators import MinValueValidator, MaxValueValidator


class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=255)
    website = models.URLField(max_length=150)
    
    def __str__(self):
        return self.name

class Watchlist(models.Model):
    title = models.CharField(max_length=55)
    storyline = models.TextField(max_length=255)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE) #user is added, so u need to add it in serializer as well
    rating = models.PositiveBigIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=255, null=True)
    watchlist = models.ForeignKey(Watchlist, on_delete=models.CASCADE, related_name="reviews")
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.rating) + " | " + self.watchlist.title