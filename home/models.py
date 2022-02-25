from django.db import models
from django.urls import reverse

from my_portfolio.utils import DRIVE_PHOTO_URL

from .validators import validate_url

# Create your models here.
class ProfessionalSummary(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_hx_edit_url(self):
        return reverse('home:hx-professional-summary-edit', kwargs={'id': self.id})


class About(models.Model):
    description = models.TextField()
    photo_url = models.CharField(max_length=200, default=DRIVE_PHOTO_URL, validators=[validate_url])
    resume_url = models.CharField(max_length=200, validators=[validate_url])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)