from django.urls import path

from game.views import (
    game_project_update_view,
    game_carousel_inline_view,
    game_carousel_delete_hx_view,
    game_carousel_form_hx_view,
)

app_name = 'game'
urlpatterns = [
    # Carousel
    # Create
    path('hx/<int:project_id>/carousel/create/', game_carousel_form_hx_view, name='hx-carousel-create'),
    # Read
    path('hx/<int:project_id>/carousel/<int:id>/', game_carousel_inline_view, name='hx-carousel-read'),
    # Update
    path('hx/<int:project_id>/carousel/<int:id>/update/', game_carousel_form_hx_view, name='hx-carousel-update'),
    # Delete
    path('hx/<int:project_id>/carousel/<int:id>/delete/', game_carousel_delete_hx_view, name='hx-carousel-delete'),

    # Project
    # Update
    path('<int:id>/update/', game_project_update_view, name='update'),
]