from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

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

def professional_summary_read_hx_view(request, id=None):
    if not request.htmx: raise Http404

    obj = get_object_or_404(ProfessionalSummary, id=id)
    context = {
        'object': obj,
    }

    return render(request, 'home/partial/professional-summary.html', context=context)

@login_required
def professional_summary_update_hx_view(request, id=None):
    if not request.htmx: raise Http404
    
    # Get the professional summary
    obj = get_object_or_404(ProfessionalSummary, id=id)

    url = obj.get_hx_edit_url()
    form = ProfessionalSummaryForm(request.POST or None, instance=obj)

    context = {
        'form': form,
        'url': url,
        'object': obj,
    }

    # When form is submitted, render home-view
    if form.is_valid():
        new_obj = form.save(commit=False)
        new_obj.save()
        context['object'] = new_obj

        return render(request, 'home/partial/professional-summary.html', context=context)

    # Render form
    return render(request, 'home/partial/professional-summary-form.html', context=context)

def about_read_view(request, id=None):
    if not request.htmx: raise Http404

    obj = get_object_or_404(About, id=id)
    context = {
        'object': obj
    }
    return render(request, 'home/partial/about.html', context=context)

@login_required
def about_update_hx_view(request, id=None):
    if not request.htmx: raise Http404
    
    # Get the about
    obj = get_object_or_404(About, id=id)

    url = obj.get_hx_edit_url()
    form = AboutForm(request.POST or None, instance=obj)

    context = {
        'form': form,
        'url': url,
        'object': obj,
    }

    # When form is submitted, render home-view
    if form.is_valid():
        new_obj = form.save(commit=False)
        new_obj.save()
        context['object'] = new_obj

        return render(request, 'home/partial/about.html', context=context)

    # Render form
    return render(request, 'home/partial/about-form.html', context=context)