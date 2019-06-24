from rest_framework import serializers
from .models import Comment, Meeting, UserProfile

class UserProfilesSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'post', 'occupation', 'year')

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('sender', 'time_of_comment', 'comment')


class MeetingSerializers(serializers.ModelSerializer):
    comments = CommentSerializers(many=True, read_only=True)

    class Meta:
        model = Meeting
        fields = ('created_by', 'time_of_creation', 'name_of_meeting', 'description_of_meeting', 'meeting_on', 'venue', 'member', 'comments')

