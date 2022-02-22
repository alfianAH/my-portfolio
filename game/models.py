from django.db import models

from home.validators import validate_url
from my_portfolio.utils import DRIVE_PHOTO_URL

# Create your models here.
class GameStatus(models.TextChoices):
    ON_GOING = 'o', 'On Going'
    COMPLETED = 'c', 'Completed'


class GameProject(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    play_url = models.CharField(max_length=200, validators=[validate_url])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class GameDetail(models.Model):
    project = models.OneToOneField(GameProject, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=GameStatus.choices, default=GameStatus.COMPLETED)
    platform = models.CharField(max_length=20)
    genre = models.CharField(max_length=100)
    engine = models.CharField(max_length=20)
    language = models.CharField(max_length=10)
    team = models.TextField()


class GameCarousel(models.Model):
    project = models.ForeignKey(GameProject, on_delete=models.CASCADE)
    url = models.CharField(max_length=200, default=DRIVE_PHOTO_URL, validators=[validate_url])


class MyProject(GameProject):
    pass


class EducationalPurposedProject(GameProject):
    pass
