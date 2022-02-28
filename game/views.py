from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .forms import GameProjectForm
from .models import EducationalPurposedProject, GameProject, MyProject

# Create your views here.
@login_required
def game_project_update_view(request, id=None):
    # If user inputs '/hx/' (for HTMX) in url, give 404
    if not request.htmx:
        print("Not HTMX")
        raise Http404
    
    obj = get_object_or_404(GameProject, id=id)
    form = GameProjectForm(request.POST or None, instance=obj)
    url = obj.get_update_url()

    # Get obj's class 
    Klasses = [MyProject, EducationalPurposedProject]
    ObjKlass = None
    for Klass in Klasses:
        qs = Klass.objects.filter(id=obj.id)

        if qs.count() >= 1:
            ObjKlass = Klass
            break
    
    context = {
        'form': form,
        'url': url,
        'game': obj,
    }

    if ObjKlass is MyProject:
        context['target'] = 'my-projects'
        context['project_title'] = 'My Projects'
    elif ObjKlass is EducationalPurposedProject:
        context['target'] = 'edu-projects'
        context['project_title'] = 'Educational Purposed Projects'
        
    if form.is_valid():
        new_obj = form.save(commit=False)
        new_obj.save()
        
        projects = ObjKlass.objects.all()
        context ['projects'] = projects
        return render(request, 'game/project-template.html', context=context)
        
    return render(request, 'game/create-update.html', context=context)
