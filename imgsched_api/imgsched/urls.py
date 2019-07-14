from django.urls import path
from rest_framework.routers import DefaultRouter
from imgsched import views
from imgsched.api import UserViewSet, CommentViewSet, MeetingViewSet

router = DefaultRouter()
router.register('meeting', MeetingViewSet, basename="Meeting")
router.register('comment', CommentViewSet)
router.register('Users', UserViewSet)
urlpatterns = router.urls

urlpatterns.append(path('home', views.index, name="home"))
urlpatterns.append(path('logout', views.logout_view))
urlpatterns.append(path('me', views.get_me))
