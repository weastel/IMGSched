from rest_framework import serializers
from .models import Comment, Meeting, UserProfile

class UserProfilesSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = __all__

class MeetingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = __all__

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = __all__