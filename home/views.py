from django.http import Http404
from django.shortcuts import render

from game.models import EducationalPurposedProject, MyProject

from .models import (
    About,
    ProfessionalSummary,
)


def home_view(request):
    """Make home view

    Args:
        request (): 

    Returns:
        any: Render page
    """
    professional_summary_qs = ProfessionalSummary.objects.all()
    about_qs = About.objects.all()

    if not professional_summary_qs.exists() or not about_qs.exists():
        return Http404
    
    my_projects = MyProject.objects.all()
    edu_projects = EducationalPurposedProject.objects.all()

    professional_summary = professional_summary_qs[0]
    about = about_qs[0]
    
    context = {
        'professional_summary': professional_summary,
        'my_projects': my_projects,
        'edu_projects': edu_projects,
        'about': about,
    }

    return render(request, 'home-view.html', context=context)
