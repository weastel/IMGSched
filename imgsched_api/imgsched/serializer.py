from rest_framework import serializers
from .models import Comment, Meeting, UserProfile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class UserProfilesSerializers(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=False)

    class Meta:
        model = UserProfile
        fields = ('user', 'post', 'occupation', 'year')


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'meeting', 'sender', 'time_of_comment', 'comment')

    def create(self, validated_data):
        print(validated_data)
        instance = Comment.objects.create(**validated_data)
        return instance


class MeetingSerializers(serializers.ModelSerializer):
    comments = CommentSerializers(many=True, read_only=True)

    class Meta:
        model = Meeting
        fields = ('id', 'created_by', 'time_of_creation', 'name_of_meeting',
                  'description_of_meeting', 'meeting_on', 'venue', 'member', 'comments')
