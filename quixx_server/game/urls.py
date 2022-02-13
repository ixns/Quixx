from django.urls import path

from . import views

app_name = "game"
urlpatterns = [
	path('', views.QuixxGamesIndexView.as_view(), name='quixx_games_index'),
	path('<int:pk>/', views.QuixxGameView.as_view(), name='quixx_single_game_view'),
]
