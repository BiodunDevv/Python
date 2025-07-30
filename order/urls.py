from django.urls import path
from order.views import HomeView
from order.views import PlayerView
from order.views import SinglePlayerView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('players/', PlayerView.as_view(), name='player_list'),
    path('players/<id>/', SinglePlayerView.as_view(), name='single_player'),
]