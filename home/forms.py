from django import forms

from home.models import About, ProfessionalSummary


class ProfessionalSummaryForm(forms.ModelForm):
    class Meta:
        model = ProfessionalSummary
        fields = ['title', 'content']
        labels = {
            'title': '',
            'content': '',
        }

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'class': 'display-5 fw-bold',
            'placeholder': 'Professional greet. Ex: Hello',
        })

        self.fields['content'].widget.attrs.update({
            'class': 'col-md-8 fs-4',
            'placeholder': 'Professional summary (max 200 chars)',
            'rows': 4,
            'style': 'resize: none'
        })


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['description', 'photo_url', 'resume_url', 
            'email', 'github_url', 'linked_in_url', 'twitter_url']
        
        labels = {
            'photo_url': 'Photo URL',
            'resume_url': 'Resume URL',
            'github_url': 'GitHub URL',
            'linked_in_url': 'LinkedIn URL',
            'twitter_url': 'Twitter URL',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        for field in self.fields:
            self.fields[str(field)].widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['description'].widget.attrs.update({
            'style': 'height: 200px',
        })

        