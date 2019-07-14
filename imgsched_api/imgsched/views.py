from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from imgsched.models import Comment, UserProfile, Meeting
from django.http import JsonResponse


def index(request):
    return render(request, "index.html")


def logout_view(request):
    logout(request)
    return redirect('react')


def get_me(request):
    if isinstance(request.user.id, (int)):
        return JsonResponse({"id": request.user.id})
    else:
        return JsonResponse({"id": "user is not authenticated"})
