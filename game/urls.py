from django.urls import path

from game.views import (
    game_project_create_view,
    game_project_update_view,
    game_project_delete_view,
    game_carousel_inline_view,
    game_carousel_delete_hx_view,
    game_carousel_form_hx_view,
)

app_name = 'game'
urlpatterns = [
    # Carousel
    # Create
    path('hx/<slug:slug>/carousel/create/', game_carousel_form_hx_view, name='hx-carousel-create'),
    # Read
    path('hx/carousel/<int:id>/', game_carousel_inline_view, name='hx-carousel-read'),
    # Update
    path('hx/<slug:slug>/carousel/<int:id>/update/', game_carousel_form_hx_view, name='hx-carousel-update'),
    # Delete
    path('hx/carousel/<int:id>/delete/', game_carousel_delete_hx_view, name='hx-carousel-delete'),

    # Project
    # Create
    path('create/<str:project_type>', game_project_create_view, name='create'),
    # Update
    path('<slug:slug>/update/', game_project_update_view, name='update'),
    # Delete
    path('<slug:slug>/delete/', game_project_delete_view, name='delete'),
]