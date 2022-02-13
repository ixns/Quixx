from django.db import models
from django.utils import timezone
from django.contrib import admin

import datetime

class QuixxGame(models.Model):
	start_date = models.DateTimeField('date game was started')

	@admin.display(
		boolean=True,
		ordering='start_date',
		description='Started recently?'
	)

	def was_started_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.start_date <= now

