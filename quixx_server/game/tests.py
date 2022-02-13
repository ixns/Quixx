import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import QuixxGame

class QuestionModelTests(TestCase):
    def test_was_started_recently_with_old_game(self):
        """
        was_started_recently() returns False for questions whose start_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_game = QuixxGame(start_date=time)
        self.assertIs(old_game.was_started_recently(), False)

    def test_was_started_recently_with_recent_game(self):
        """
        was_started_recently() returns True for questions whose start_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_game = QuixxGame(start_date=time)
        self.assertIs(recent_game.was_started_recently(), True)

    def test_was_published_recently_with_future_question(self):
        """
        was_started_recently() returns False for questions whose start_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_game = QuixxGame(start_date=time)
        self.assertIs(future_game.was_started_recently(), False)
