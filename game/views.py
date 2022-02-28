from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .forms import GameCarouselForm, GameDetailForm, GameProjectForm
from .models import EducationalPurposedProject, GameCarousel, GameDetail, GameProject, MyProject

# Create your views here.
@login_required
def game_project_update_view(request, id=None):
    # If user inputs '/hx/' (for HTMX) in url, give 404
    if not request.htmx:
        raise Http404
    
    obj = get_object_or_404(GameProject, id=id)
    form = GameProjectForm(request.POST or None, instance=obj)
    url = obj.get_update_url()

    # Game detail form
    game_detail_form = GameDetailForm(request.POST or None, instance=obj.get_game_detail())

    # Game carousel formset
    GameCarouselFormset = modelformset_factory(model=GameCarousel, form=GameCarouselForm, extra=0)
    game_carousel_formset = GameCarouselFormset(request.POST or None, queryset=obj.get_game_carousel_qs())

    # Get obj's class (Game Project)
    Klasses = [MyProject, EducationalPurposedProject]
    ObjKlass = None
    for Klass in Klasses:
        qs = Klass.objects.filter(id=obj.id)

        if qs.count() >= 1:
            ObjKlass = Klass
            break

    context = {
        'form': form,
        'game_detail_form': game_detail_form,
        'game_carousel_formset': game_carousel_formset,
        'url': url,
        'game': obj,
    }
    
    # Validate game project's class
    if ObjKlass is MyProject:
        context['target'] = 'my-projects'
        context['project_title'] = 'My Projects'
    elif ObjKlass is EducationalPurposedProject:
        context['target'] = 'edu-projects'
        context['project_title'] = 'Educational Purposed Projects'

    # Save form if it is valid  
    if all([
        form.is_valid(), 
        game_detail_form.is_valid(), 
        game_carousel_formset.is_valid(),
    ]):
        new_obj = form.save(commit=False)
        new_obj.save()

        # Game detail forms
        game_detail = game_detail_form.save(commit=False)
        if not hasattr(game_detail, 'project'):
            game_detail.project = new_obj
        game_detail.save()
        
        # Game carousel forms
        for form in game_carousel_formset:
            game_carousel = form.save(commit=False)
            if not hasattr(game_carousel, 'project'):
                game_carousel.project = new_obj
            game_carousel.save()
        
        projects = ObjKlass.objects.all()
        context ['projects'] = projects
        return render(request, 'game/project-template.html', context=context)
        
    return render(request, 'game/create-update.html', context=context)
