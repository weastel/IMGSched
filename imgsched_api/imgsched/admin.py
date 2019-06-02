from django.contrib import admin
from .models import UserProfile, Meeting, Comment

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Meeting)
admin.site.register(Comment)