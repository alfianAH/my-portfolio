from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if form.is_valid():
        login(request, form.get_user())
        return redirect('/')

    context = {'form': form}

    return render(request, 'accounts/login.html', context=context)

def logout_hx_view(request):
    # If user inputs '/hx/' (for HTMX) in url, give 404
    if not request.htmx:
        raise Http404
    
    if request.method == 'POST':
        logout(request)
        success_url = '/accounts/login/'

        if request.htmx:
            headers = {
                'hx-redirect': success_url
            }

            return HttpResponse("Success", headers=headers)

        return redirect(success_url)
    
    return render(request, 'accounts/logout-modal.html')