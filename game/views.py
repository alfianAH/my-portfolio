from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from .forms import GameCarouselForm, GameDetailForm, GameProjectForm
from .models import (
    EducationalPurposedProject, 
    GameCarousel, 
    GameDetail, 
    GameProject, 
    MyProject
)

# Create your views here.
@login_required
def game_project_delete_view(request, slug=None):
    # If user inputs '/hx/' (for HTMX) in url, give 404
    if not request.htmx:
        raise Http404
    
    obj = get_object_or_404(GameProject, slug=slug)
    obj_title = obj.title
    obj_slug = obj.slug
    print('get')
    if request.htmx:
        print('delete')
        # obj.delete()
        context = {
            'id': 'toast-{}'.format(obj_slug),
            'content': 'Game "{}" deleted'.format(obj_title)
        }
        return render(request, 'components/toast-template.html', context=context)

@login_required
def game_project_update_view(request, slug=None):
    # If user inputs '/hx/' (for HTMX) in url, give 404
    if not request.htmx:
        raise Http404
    
    obj = get_object_or_404(GameProject, slug=slug)
    form = GameProjectForm(request.POST or None, instance=obj)
    url = obj.get_update_url()

    # Game detail form
    game_detail_form = GameDetailForm(request.POST or None, instance=obj.get_game_detail())

    # Game carousel url
    game_carousel_create_url = obj.get_create_carousel_url()

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
        'game_carousel_create_url': game_carousel_create_url,
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
        game_detail_form.is_valid()
    ]):
        new_obj = form.save(commit=False)
        new_obj.save()

        # Game detail forms
        game_detail = game_detail_form.save(commit=False)
        if not hasattr(game_detail, 'project'):
            game_detail.project = new_obj
        game_detail.save()
        
        projects = ObjKlass.objects.all()
        context ['projects'] = projects
        return render(request, 'game/project-template.html', context=context)
        
    return render(request, 'game/create-update.html', context=context)

def game_carousel_inline_view(request, slug=None, id=None):
    # If user inputs '/hx/' (for HTMX) in url, give 404
    if not request.htmx:
        raise Http404
    
    # Get carousel object
    carousel_obj = get_object_or_404(GameCarousel, project__slug=slug, id=id)
    
    context = {
        'object': carousel_obj,
    }

    return render(request, 'game/partial/carousel-inline.html', context=context)

@login_required
def game_carousel_form_hx_view(request, slug=None, id=None):
    # If user inputs '/hx/' (for HTMX) in url, give 404
    if not request.htmx:
        raise Http404

    # Get project object
    try:
        project_obj = GameProject.objects.get(slug=slug)
    except:
        project_obj = None

    # If there are no objects, return not found
    if project_obj is None:
        return HttpResponse('Game project not found')
    
    # Get carousel id if not None (case: Update carousel)
    carousel_obj = None
    if id is not None:
        try:
            carousel_obj = GameCarousel.objects.get(id=id)
        except:
            carousel_obj = None

    # Pass create URL (default)
    url = project_obj.get_create_carousel_url()

    # If update carousel, pass update URL
    if carousel_obj:
        url = carousel_obj.get_update_carousel_url()

    form = GameCarouselForm(request.POST or None, instance=carousel_obj)

    context = {
        'url': url,
        'object': carousel_obj,
        'form': form,
    }

    if form.is_valid():
        new_obj = form.save(commit=False)

        # If create new one, assign project
        if carousel_obj is None:
            new_obj.project = project_obj
        
        new_obj.save()
        context['object'] = new_obj
        # Render inline
        return render(request, 'game/partial/carousel-inline.html', context=context)
    
    # Render form
    return render(request, 'game/partial/carousel-form.html', context=context)

@login_required
def game_carousel_delete_hx_view(request, slug=None, id=None):
    # If user inputs '/hx/' (for HTMX) in url, give 404
    if not request.htmx:
        raise Http404
    
    carousel_obj = get_object_or_404(GameCarousel, project__slug=slug, id=id)

    if request.htmx:
        carousel_obj.delete()

        return render(request, 'game/partial/carousel-delete-inline-response.html')
