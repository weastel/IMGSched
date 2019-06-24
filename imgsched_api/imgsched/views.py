from rest_framework import generics
from imgsched.models import Comment, UserProfile, Meeting
from imgsched.serializer import CommentSerializers, UserProfilesSerializers, MeetingSerializers


class ProfileList(generics.ListCreateAPIView):
        queryset = UserProfile.objects.all()
        serializer_class = UserProfilesSerializers

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = UserProfile.objects.all()
        serializer_class = UserProfilesSerializers

class MeetingList(generics.ListCreateAPIView):
        queryset = Meeting.objects.all()
        serializer_class = MeetingSerializers

class MeetingDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Meeting.objects.all()
        serializer_class = MeetingSerializers

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Comment.objects.all()
        serializer_class = CommentSerializers
