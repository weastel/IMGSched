from django.contrib import admin
from .models import UserProfile, Meeting, Comment, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class WebsiteUsers(admin.StackedInline):
    model = UserProfile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = (WebsiteUsers,)

# Register your models here.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Meeting)
admin.site.register(Comment)