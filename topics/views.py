from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Topics
from .serializers import TopicsSerializer
from fr_drf_api.permissions import IsOwnerOrReadOnly


class TopicsList(APIView):
    serializer_class = TopicsSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        topics = Topics.objects.all()
        serializer = TopicsSerializer(
            topics, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = TopicsSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class TopicsDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TopicsSerializer

    def get_object(self, pk):
        try:
            topic = Topics.objects.get(pk=pk)
            self.check_object_permissions(self.request, topic)
            return topic
        except Topics.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        topic = self.get_object(pk)
        serializer = TopicsSerializer(
            topic, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        topic = self.get_object(pk)
        serializer = TopicsSerializer(
            topic, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        topic = self.get_object(pk)
        topic.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )