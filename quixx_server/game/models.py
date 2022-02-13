from django.db import models
import datetime
import ../globals

class QuixxGame(models.Model):
	start_date = models.DateTimeField('date game was started')
	player_count = models.IntegerField('the number of players in the game')
	player_1 = models.CharField(max_length=globals.max_username_length)		
	player_2 = models.CharField(max_length=globals.max_username_length)		
	player_3 = models.CharField(max_length=globals.max_username_length)		
	player_4 = models.CharField(max_length=globals.max_username_length)		

	
	

	@admin.display(
		boolean=True,
		ordering='start_date',
		description='Started recently?'
	)

	def was_started_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.start_date <= now

