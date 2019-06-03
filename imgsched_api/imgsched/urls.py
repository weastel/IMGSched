from django.urls import path
from imgsched import views

urlpatterns = [
    path('profile', views.profile_list),
    path('profile/<int:pk>/', views.specfic_profile),
    path('meeting', views.meeting_list),
    path('meeting/<int:pk>/', views.specific_meeting)
]
