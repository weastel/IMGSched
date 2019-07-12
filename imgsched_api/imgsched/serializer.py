from rest_framework import serializers
from .models import Comment, Meeting, UserProfile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name')

class UserProfilesSerializers(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=False)
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

