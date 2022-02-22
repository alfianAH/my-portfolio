from django.db import models

from my_portfolio.utils import DRIVE_PHOTO_URL

from .validators import validate_url

# Create your models here.
class ProfessionalSummary(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class About(models.Model):
    description = models.TextField()
    photo_url = models.CharField(max_length=200, default=DRIVE_PHOTO_URL, validators=[validate_url])
    resume_url = models.CharField(max_length=200, validators=[validate_url])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)