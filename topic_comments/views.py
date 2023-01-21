from rest_framework import generics, permissions
from fr_drf_api.permissions import IsOwnerOrReadOnly
from .models import TopicComment
from .serializers import TopicCommentSerializer, TopicCommentDetailSerializer


class TopicCommentList(generics.ListCreateAPIView):
    """
    List topic comments or create a topic comment if logged in.
    """
    serializer_class = TopicCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = TopicComment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TopicCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a topic comment, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TopicCommentDetailSerializer
    queryset = TopicComment.objects.all()
