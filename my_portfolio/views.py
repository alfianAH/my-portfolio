"""
To render HTML web page
"""

from django.shortcuts import render


def home_view(request):
    """
    Make home view
    @param request: Django's request
    @return: Returns HTML as a response
    """
    
    # Django templates
    html_fn = "home-view.html"
    return render(request, html_fn)
