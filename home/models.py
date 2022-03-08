from django.db import models
from django.urls import reverse
from django.core.validators import validate_email

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

    def get_hx_read_url(self):
        return reverse('home:hx-professional-summary-read', kwargs={'id': self.id})


class About(models.Model):
    description = models.TextField()
    photo_url = models.CharField(max_length=200, default=DRIVE_PHOTO_URL, validators=[validate_url])
    resume_url = models.CharField(max_length=200, validators=[validate_url])

    email = models.CharField(max_length=200, blank=True, null=True, validators=[validate_email])
    github_url = models.CharField(max_length=200, blank=True, null=True, validators=[validate_url])
    linked_in_url = models.CharField(max_length=200, blank=True, null=True, validators=[validate_url])
    twitter_url = models.CharField(max_length=200, blank=True, null=True, validators=[validate_url])

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_hx_edit_url(self):
        return reverse('home:hx-about-edit', kwargs={'id': self.id})
    
    def get_hx_read_url(self):
        return reverse('home:hx-about-read', kwargs={'id': self.id})