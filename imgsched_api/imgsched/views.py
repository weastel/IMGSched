from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from imgsched.models import Comment, UserProfile, Meeting
from imgsched.serializer import CommentSerializers, UserProfilesSerializers, MeetingSerializers 

@csrf_exempt
def profile_list(request):
    if request.method == "GET":
        profile = UserProfile.objects.all()
        serializer = UserProfilesSerializers(profile, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def specfic_profile(request, pk):
    if request.method == "GET":
        profile = UserProfile.objects.get(pk=pk)
        serializer = UserProfilesSerializers(profile)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def meeting_list(request):
    if request.method == "GET":
        meeting = Meeting.objects.all()
        serializer = MeetingSerializers(meeting, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def specific_meeting(request, pk):
    if request.method == "GET":
        meeting = Meeting.objects.get(pk=pk)
        serializer = MeetingSerializers(meeting)
        return JsonResponse(serializer.data, safe=False)
