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
            query = Q(member=self.request.user.id)
            query.add(Q(created_by=self.request.user.id), Q.OR)
            queryset = Meeting.objects.filter(
                query)
        return queryset


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfilesSerializers
    queryset = UserProfile.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializers
    queryset = Comment.objects.all()
