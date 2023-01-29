from rest_framework import serializers
from .models import Profile
from followers.models import Follower
from topics.models import Topics
from topic_comments.models import TopicComment


# class taken from DRF-APi walkthrough with modifications
class ProfileSerializer(serializers.ModelSerializer):
    '''profile serializer class'''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    comment_count = serializers.ReadOnlyField()
    topic_count = serializers.ReadOnlyField()
    topic_comment_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        ''' check user is owner '''
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'bio', 'image', 'fan_or_club', 'official', 'support',
            'is_owner', 'following_id', 'posts_count',
            'followers_count', 'following_count', 'comment_count',
            'topic_count', 'topic_comment_count',
        ]
