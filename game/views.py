from django.http import Http404
from django.shortcuts import render

from game.models import GameProject

# Create your views here.
def game_project_detail_view(request, slug=None):
    project_obj = None

    if slug is not None:
        try:
            project_obj = GameProject.objects.get(slug=slug)
        except GameProject.DoesNotExist:
            raise Http404
        except GameProject.MultipleObjectsReturned:
            project_obj = GameProject.objects.filter(slug=slug).first()
        except:
            raise Http404

    context = {
        'game': project_obj
    }

    return render(request, 'game/detail.html', context=context)
