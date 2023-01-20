from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    CLUB = 'Club'
    FAN = 'Fan'
    CLUB_OR_FAN_CHOICES = [
        (CLUB, 'Club'),
        (FAN, 'Fan'),
    ]
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    fan_or_club = models.CharField(choices=CLUB_OR_FAN_CHOICES, default=FAN,)
    image = models.ImageField(
        upload_to='images/', default='../ball-flying_oncxm2')
    official = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
