from django.db import models
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

from .utils import slugify_instance_title
from home.validators import validate_url
from my_portfolio.utils import DRIVE_PHOTO_URL

# Create your models here.
class GameStatus(models.TextChoices):
    ON_GOING = 'o', 'On Going'
    COMPLETED = 'c', 'Completed'


class GameProject(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    play_url = models.CharField(max_length=200, validators=[validate_url])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_detail_url(self):
        return reverse('game:detail', kwargs={'slug': self.slug})


class GameDetail(models.Model):
    project = models.OneToOneField(GameProject, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=GameStatus.choices, default=GameStatus.COMPLETED)
    platform = models.CharField(max_length=20)
    genre = models.CharField(max_length=100)
    engine = models.CharField(max_length=20, default='Unity')
    language = models.CharField(max_length=10, default='C#')
    team = models.TextField()

    def parse_team(self):
        return self.team.split(',')


class GameCarousel(models.Model):
    project = models.ForeignKey(GameProject, on_delete=models.CASCADE)
    url = models.CharField(max_length=200, default=DRIVE_PHOTO_URL, validators=[validate_url])


class MyProject(GameProject):
    pass


class EducationalPurposedProject(GameProject):
    pass


def project_pre_save(sender, instance, *args, **kwargs):    
    if instance.slug is None:
        slugify_instance_title(instance)

def project_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_title(instance, save=True)


pre_save.connect(project_pre_save, sender=EducationalPurposedProject)
post_save.connect(project_post_save, sender=EducationalPurposedProject)
pre_save.connect(project_pre_save, sender=MyProject)
post_save.connect(project_post_save, sender=MyProject)
