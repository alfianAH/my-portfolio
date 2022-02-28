from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import render

from game.models import EducationalPurposedProject, MyProject
from home.forms import AboutForm, ProfessionalSummaryForm

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

    return render(request, 'home/home-view.html', context=context)

@login_required
def professional_summary_update_hx_view(request, id=None):
    if not request.htmx: raise Http404
    
    # Get the professional summary
    if id is not None:
        try:
            obj = ProfessionalSummary.objects.get(id=id)
        except:
            obj = None

    # Return not found if obj is none
    if obj is None:
        return HttpResponse('Professional summary is not found')

    url = obj.get_hx_edit_url()
    form = ProfessionalSummaryForm(request.POST or None, instance=obj)

    context = {
        'form': form,
        'url': url,
        'professional_summary': obj,
    }

    # When form is submitted, render home-view
    if form.is_valid():
        new_obj = form.save(commit=False)
        new_obj.save()
        context['professional_summary'] = new_obj

        return render(request, 'home/partial/professional-summary.html', context=context)

    # Render form
    return render(request, 'home/partial/normal-form.html', context=context)

@login_required
def about_update_hx_view(request, id=None):
    if not request.htmx: raise Http404
    
    # Get the professional summary
    if id is not None:
        try:
            obj = About.objects.get(id=id)
        except:
            obj = None

    # Return not found if obj is none
    if obj is None:
        return HttpResponse('About is not found')

    url = obj.get_hx_edit_url()
    form = AboutForm(request.POST or None, instance=obj)

    context = {
        'form': form,
        'url': url,
        'about': obj,
    }

    # When form is submitted, render home-view
    if form.is_valid():
        new_obj = form.save(commit=False)
        new_obj.save()
        context['about'] = new_obj

        return render(request, 'home/partial/about.html', context=context)

    # Render form
    return render(request, 'home/partial/about-form.html', context=context)