from rest_framework import generics, permissions
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
    queryset = Topics.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TopicsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = TopicsSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Topics.objects.all()