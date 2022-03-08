from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from game.models import EducationalPurposedProject, MyProject
from home.forms import AboutForm, ProfessionalSummaryForm

from .models import (
    About,
    ProfessionalSummary,
)


def home_view(request):
    professional_summary_qs = ProfessionalSummary.objects.all()
    about_qs = About.objects.all()

    if not professional_summary_qs.exists() or not about_qs.exists():
        return redirect('home:setup')
    
    my_projects = MyProject.objects.all().order_by('-release_date', 'title')
    edu_projects = EducationalPurposedProject.objects.all().order_by('-release_date', 'title')

    professional_summary = professional_summary_qs[0]
    about = about_qs[0]
    
    context = {
        'professional_summary': professional_summary,
        'my_projects': my_projects,
        'edu_projects': edu_projects,
        'about': about,
    }

    return render(request, 'home/home-view.html', context=context)

def setup_view(request):
    prof_summary_obj = ProfessionalSummary.objects.all()
    about_obj = About.objects.all()

    # If there are already prof summary and about, redirect to home
    if prof_summary_obj.exists() and about_obj.exists():
        return redirect('/home/')
    
    # Default forms
    professional_summary_form = ProfessionalSummaryForm(request.POST or None)
    about_form = AboutForm(request.POST or None)

    # Form that one of the object exists
    if prof_summary_obj.exists() and not about_obj.exists():
        professional_summary_form = ProfessionalSummaryForm(request.POST or None, instance=prof_summary_obj[0])
    elif not prof_summary_obj.exists() and about_obj.exists():
        about_form = AboutForm(request.POST or None, instance=about_obj[0])

    context = {
        'professional_summary_form': professional_summary_form,
        'about_form': about_form,
    }

    if all([
        professional_summary_form.is_valid(),
        about_form.is_valid(),
    ]):
        prof_summary_obj = professional_summary_form.save(commit=False)
        prof_summary_obj.save()

        about_obj = about_form.save(commit=False)
        about_obj.save()

        print("Save")

        return redirect('/home/')

    return render(request, 'home/setup-view.html', context=context)

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