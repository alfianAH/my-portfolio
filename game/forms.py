from django import forms
from .models import (
    EducationalPurposedProject,
    GameProject,
    GameCarousel,
    GameDetail,
    MyProject
)


class GameProjectForm(forms.ModelForm):
    class Meta:
        model = GameProject
        fields = ['title', 'description', 'play_url']


class MyProjectForm(forms.ModelForm):
    class Meta:
        model = MyProject
        fields = ['title', 'description', 'play_url']


class EducationalPurposedProjectForm(forms.ModelForm):
    class Meta:
        model = EducationalPurposedProject
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