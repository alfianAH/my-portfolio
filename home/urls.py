from django.urls import path

from home.views import (
    home_view, 
    professional_summary_update_hx_view,
)


app_name = 'home'
urlpatterns = [
    path('', home_view),
    path('hx/prof-summary/<int:id>', professional_summary_update_hx_view, name='hx-professional-summary-edit')
]