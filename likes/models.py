from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from topics.models import Topics
from topic_comments.models import TopicComment
from comments.models import Comment


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

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post',]

    def __str__(self):
        return f'{self.owner} {self.post}'


class LikeComment(models.Model):
    """
    Like model, related to 'owner' and 'post' or 'topic post.
    'owner' is a User instance and 'post' or 'topic post is a Post instance.
    'unique_together' makes sure a user can't like the same post twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(
        Comment, related_name='likes', on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'comment']

    def __str__(self):
        return f'{self.owner} {self.comment}'


class LikeTopic(models.Model):
    """
    Like model, related to 'owner' and 'post' or 'topic post.
    'owner' is a User instance and 'post' or 'topic post is a Post instance.
    'unique_together' makes sure a user can't like the same post twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Topics, related_name='likes', on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'


class LikeTopicComment(models.Model):
    """
    Like model, related to 'owner' and 'post' or 'topic post.
    'owner' is a User instance and 'post' or 'topic post is a Post instance.
    'unique_together' makes sure a user can't like the same post twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(
        TopicComment, related_name='likes', on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'comment']

    def __str__(self):
        return f'{self.owner} {self.comment}'
