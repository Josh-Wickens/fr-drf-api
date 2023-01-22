from rest_framework import serializers
from topics.models import Topics
from likes.models import LikeTopic


class TopicsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    official = serializers.ReadOnlyField(source='owner.profile.official')
    fan_or_club = serializers.ReadOnlyField(source='owner.profile.fan_or_club')
    like_id = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = LikeTopic.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Topics
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'question', 'image', 'topic', 'official',
            'fan_or_club', 'like_id'
        ]
