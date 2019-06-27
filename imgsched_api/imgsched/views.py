from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from imgsched.models import Comment, UserProfile, Meeting
from imgsched.serializer import CommentSerializers, UserProfilesSerializers, MeetingSerializers


class ProfileList(generics.ListCreateAPIView):
        permission_classes = (IsAuthenticated,)
        queryset = UserProfile.objects.all()
        serializer_class = UserProfilesSerializers

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
        permission_classes = (IsAuthenticated,)
        queryset = UserProfile.objects.all()
        serializer_class = UserProfilesSerializers

class MeetingList(generics.ListCreateAPIView):
        permission_classes = (IsAuthenticated,)
        queryset = Meeting.objects.all()
        serializer_class = MeetingSerializers

class MeetingDetail(generics.RetrieveUpdateDestroyAPIView):
        permission_classes = (IsAuthenticated,)
        queryset = Meeting.objects.all()
        serializer_class = MeetingSerializers

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
        permission_classes = (IsAuthenticated,)
        queryset = Comment.objects.all()
        serializer_class = CommentSerializers

def index(request):
        return render(request,"index.html")

def logout_view(request):
        logout(request)
        return redirect('home')