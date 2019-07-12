from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from imgsched.models import Comment, UserProfile, Meeting


def index(request):
        return render(request,"index.html")

def logout_view(request):
        logout(request)
        return redirect('home')