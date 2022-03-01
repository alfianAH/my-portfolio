from django import forms
from .models import (
    GameProject,
    GameCarousel,
    GameDetail
)


class GameProjectForm(forms.ModelForm):
    class Meta:
        model = GameProject
        fields = ['title', 'description', 'play_url']


class GameDetailForm(forms.ModelForm):
    class Meta:
        model = GameDetail
        fields = ['status', 'platform', 'genre', 'engine', 'language', 'team']


class GameCarouselForm(forms.ModelForm):
    class Meta: 
        model = GameCarousel
        fields = ['url']
        labels = {'url': 'URL'}