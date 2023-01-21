from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from topics.models import Topics


class Like(models.Model):
    """
    Like model, related to 'owner' and 'post' or 'topic post.
    'owner' is a User instance and 'post' or 'topic post is a Post instance.
    'unique_together' makes sure a user can't like the same post twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='likes', on_delete=models.CASCADE
    )
    topic_post = models.ForeignKey(
        Topics, related_name='likes', on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post',]
        unique_together = ['owner', 'topic_post']

    def __str__(self):
        return f'{self.owner} {self.post or self.topic_post}'
