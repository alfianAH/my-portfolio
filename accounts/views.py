from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if form.is_valid():
        login(request, form.get_user())
        return redirect('/')

    context = {'form': form}

    return render(request, 'accounts/login.html', context=context)

def logout_view(request):
    if request.htmx:
        logout(request)
        headers = {
            'hx-redirect': '/'
        }
        return HttpResponse("Success", headers=headers)
    
    if request.method == 'POST':
        logout(request)
        return redirect('/login/')
    
    return render(request, 'accounts/logout.html')