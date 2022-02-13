from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views.generic import *

from .models import QuixxGame

class QuixxGamesIndexView(ListView):
	template_name = 'game/index.html'
	context_object_name = 'latest_games_list'

	def get_queryset(self):
		"""
		Return all open Quixx games
		"""
		return QuixxGame.objects
	

class QuixxGameView(DetailView):
	model = QuixxGame
	template_name = 'game/game.html'
	
	def get_queryset(self):
		"""
		Excludes games that aren't published yet.
		"""
		return QuixxGame.objects.filter(pub_date__lte=timezone.now())
	
