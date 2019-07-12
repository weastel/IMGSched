from rest_framework import viewsets
from .serializer import UserProfilesSerializers, MeetingSerializers, CommentSerializers
from .models import Meeting, UserProfile,  Comment
from django.db.models import Q
from django.contrib.auth.models import User

class MeetingViewSet(viewsets.ModelViewSet):
    serializer_class = MeetingSerializers
    def get_queryset(self):
        usersprofile = UserProfile.objects.get(pk=self.request.user.id)
        if usersprofile.post == 'A':
            queryset = Meeting.objects.all()
        else:
            queryset = Meeting.objects.filter(Q(member=self.request.user.id) | Q(created_by=self.request.user.id) )
        return queryset


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfilesSerializers
    queryset = UserProfile.objects.all()

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializers
    queryset = Comment.objects.all()