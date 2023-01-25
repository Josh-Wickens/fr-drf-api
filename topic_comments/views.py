from django.db.models import Count
from rest_framework import generics, permissions, filters
from fr_drf_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import TopicComment
from .serializers import TopicCommentSerializer, TopicCommentDetailSerializer


class TopicCommentList(generics.ListCreateAPIView):
    """
    List topic comments or create a topic comment if logged in.
    """
    serializer_class = TopicCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = TopicComment.objects.annotate(
        likes_count=Count('likes', distinct=True)
        ).order_by('-created_at')
    filter_backends = [DjangoFilterBackend]
    ordering_fields = [
        'likes_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TopicCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a topic comment, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TopicCommentDetailSerializer
    queryset = TopicComment.objects.all()
