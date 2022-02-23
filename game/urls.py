from django.urls import path

from .views import game_project_detail_view


app_name = 'game'
urlpatterns = [
    # path('create/', , name='create'),
    path('<slug:slug>/', game_project_detail_view, name='detail'),
]