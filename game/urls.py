from django.urls import path

from game.views import game_project_update_view

app_name = 'game'
urlpatterns = [
    # path('create/', , name='create'),
    path('<int:id>/update/', game_project_update_view, name='update'),
]