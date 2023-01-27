from django.db import models
from django.contrib.auth.models import User


class Topics(models.Model):
    # GENERAL = 'General'
    # PLAYERS = 'Players'
    # TEAMS = 'Teams'
    # TRANSFERS = 'Transfers'
    # FIXTURES = 'Fixtures'
    # RESULTS = 'Results'
    # TOPIC_CHOICES = [
    #     (GENERAL, 'General'),
    #     (PLAYERS, 'Players'),
    #     (TEAMS, 'Teams'),
    #     (TRANSFERS, 'Transfers'),
    #     (FIXTURES, 'Fixtures'),
    #     (RESULTS, 'Results'),
    # ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    topic = models.CharField(max_length=30, blank=False)
    question = models.CharField(max_length=400, blank=False)
    image = models.ImageField(
        upload_to='images/', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.question}'
