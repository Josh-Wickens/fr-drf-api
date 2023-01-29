from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# some code provided by DRF-API walkthrough
# modifications made for this project


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
    bio = models.TextField(max_length=500, default="This is my Bio", blank=True)
    fan_or_club = models.CharField(
        choices=CLUB_OR_FAN_CHOICES, max_length=10, default=FAN,)
    image = models.ImageField(
        upload_to='images/', default='../ball-flying_xiyzfz')
    official = models.BooleanField(default=False)
    support = models.CharField(max_length=30, default="Football", blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


# function taken from DRF-API walkthroug
def create_profile(sender, instance, created, **kwargs):
    ''' ensure a profile is created for each user created '''
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
