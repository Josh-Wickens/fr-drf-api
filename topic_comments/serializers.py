from rest_framework import serializers
from .models import TopicComment


class TopicCommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Topic Comment model
    Adds three extra fields when returning a list of Comment instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    official = serializers.ReadOnlyField(source='owner.profile.official')
    fan_or_club = serializers.ReadOnlyField(source='owner.profile.fan_or_club')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = TopicComment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'post', 'created_at', 'updated_at', 'content', 'official',
            'fan_or_club'
        ]


class TopicCommentDetailSerializer(TopicCommentSerializer):
    """
    Serializer for the TopicComment model used in Detail view
    Post is a read only field so that we dont have to set it on each update
    """
    topic = serializers.ReadOnlyField(source='topic.id')