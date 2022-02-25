from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .forms import GameProjectForm
from .models import GameProject

# Create your views here.
@login_required
def game_project_update_view(request, id=None):
    obj = get_object_or_404(GameProject, id=id)
    form = GameProjectForm(request.POST or None, instance=obj)

    context = {
        'form': form,
        'game': obj,
    }

    if form.is_valid():
        form.save()

    print(request)
        
    return render(request, 'game/create-update.html', context=context)
