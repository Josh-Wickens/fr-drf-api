from django.db.models import Count
from rest_framework import generics, permissions, filters
from fr_drf_api.permissions import IsOwnerOrReadOnly
from .models import Topics
from .serializers import TopicsSerializer


class TopicsList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = TopicsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Topics.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('topiccomment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'owner__username',
        'topic',
        'owner__profile__fan_or_club',
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TopicsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = TopicsSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Topics.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('topiccomment', distinct=True)
    ).order_by('-created_at')
