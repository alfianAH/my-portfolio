from django.urls import path

from home.views import (
    home_view, 
    professional_summary_read_hx_view,
    professional_summary_update_hx_view,
    about_read_view,
    about_update_hx_view,
)


app_name = 'home'
urlpatterns = [
    path('', home_view),
    path('hx/prof-summary/<int:id>', professional_summary_read_hx_view, name='hx-professional-summary-read'),

    path('hx/prof-summary/<int:id>/edit', professional_summary_update_hx_view, name='hx-professional-summary-edit'),

    path('hx/about/<int:id>', about_read_view, name='hx-about-read'),
    path('hx/about/<int:id>/edit', about_update_hx_view, name='hx-about-edit')
]