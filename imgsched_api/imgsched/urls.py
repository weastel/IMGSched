from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from imgsched import views

urlpatterns = [
    path('profile', views.ProfileList.as_view()),
    path('profile/<int:pk>/', views.ProfileDetail.as_view()),
    path('meeting', views.MeetingList.as_view()),
    path('meeting/<int:pk>/', views.MeetingDetail.as_view()),
    path('', views.index, name='home'),
    path('logout', views.logout_view)
]

urlpatterns = format_suffix_patterns(urlpatterns)
