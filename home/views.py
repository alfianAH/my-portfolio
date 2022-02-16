from django.http import Http404
from django.shortcuts import render

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
    
    professional_summary = professional_summary_qs[0]
    about = about_qs[0]
    
    context = {
        'professional_summary': professional_summary,
        'about': about
    }

    return render(request, 'home-view.html', context=context)
