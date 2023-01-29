from rest_framework import generics, permissions
from fr_drf_api.permissions import IsOwnerOrReadOnly
from likes.models import Like, LikeTopic, LikeTopicComment, LikeComment
from likes.serializers import LikeSerializer, LikeTopicSerializer, LikeTopicCommentSerializer, LikeCommentSerializer


class LikeList(generics.ListCreateAPIView):
    """
    List likes or create a like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()


class LikeTopicList(generics.ListCreateAPIView):
    """
    List topic likes or create a topic like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeTopicSerializer
    queryset = LikeTopic.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeTopicDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a topic like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeTopicSerializer
    queryset = LikeTopic.objects.all()


class LikeTopicCommentList(generics.ListCreateAPIView):
    """
    List topic comment likes or create a like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeTopicCommentSerializer
    queryset = LikeTopicComment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeTopicCommentDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a topic comment like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeTopicCommentSerializer
    queryset = LikeTopicComment.objects.all()


class LikeCommentList(generics.ListCreateAPIView):
    """
    List comment likes or create a like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeCommentSerializer
    queryset = LikeComment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeCommentDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a comment like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeCommentSerializer
    queryset = LikeComment.objects.all()
