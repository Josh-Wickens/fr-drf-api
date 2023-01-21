from django.db import models
from django.contrib.auth.models import User
from topics.models import Topics


class TopicComment(models.Model):
    """
    Topic Comment model, related to User and Topics
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Topics, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
