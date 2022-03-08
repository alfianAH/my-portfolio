from django import forms
from .models import (
    EducationalPurposedProject,
    GameProject,
    GameCarousel,
    GameDetail,
    MyProject
)

class DateInput(forms.DateInput):
    input_type = 'date'


class GameProjectForm(forms.ModelForm):
    class Meta:
        model = GameProject
        fields = ['title', 'release_date', 'description', 'play_url']
        widgets = {
            'release_date': DateInput()
        }


class MyProjectForm(forms.ModelForm):
    class Meta:
        model = MyProject
        fields = ['title', 'release_date', 'description', 'play_url']
        widgets = {
            'release_date': DateInput()
        }


class EducationalPurposedProjectForm(forms.ModelForm):
    class Meta:
        model = EducationalPurposedProject
        fields = ['title', 'release_date', 'description', 'play_url']
        widgets = {
            'release_date': DateInput()
        }


class GameDetailForm(forms.ModelForm):
    class Meta:
        model = GameDetail
        fields = ['status', 'platform', 'genre', 'engine', 'language', 'team']


class GameCarouselForm(forms.ModelForm):
    class Meta: 
        model = GameCarousel
        fields = ['url']
        labels = {'url': 'URL'}