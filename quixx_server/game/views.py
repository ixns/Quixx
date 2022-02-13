from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views.generic import *

from .models import QuixxGame

class QuixxGamesIndexView(ListView):
	template_name = 'game/index.html'
	context_object_name = 'games_list'

	def get_queryset(self):
		"""
		Return all open Quixx games
		"""
		return QuixxGame.objects.filter(
            start_date__lte=timezone.now()
        ).order_by('-start_date')[:5]
	

class QuixxGameView(DetailView):
	model = QuixxGame
	template_name = 'game/game.html'
	
	def get_queryset(self):
		"""
		Excludes games that aren't started yet.
		"""
		return QuixxGame.objects.filter(start_date__lte=timezone.now())
	
