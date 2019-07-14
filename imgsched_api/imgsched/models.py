from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class UserProfile (models.Model):
    user_post = [
        ('A', 'admin'),
        ('U', 'user')
    ]
    user_occupation = [
        ('dev', 'developer'),
        ('des', 'designer')
    ]
    user_year = [
        ('1', 'first_year'),
        ('2', 'second_year'),
        ('3', 'third_year'),
        ('4', 'fourth_year'),
        ('5', 'fifth_year')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    post = models.CharField(max_length=1, choices=user_post)
    occupation = models.CharField(max_length=3, choices=user_occupation)
    year = models.CharField(max_length=1, choices=user_year)

    def __str__(self):
        return self.user.username


class Meeting (models.Model):
    created_by = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="creator")
    time_of_creation = models.DateTimeField(default=timezone.now)
    name_of_meeting = models.CharField(max_length=254)
    description_of_meeting = models.TextField()
    meeting_on = models.DateTimeField()
    venue = models.CharField(max_length=254, default='IMG Lab')
    member = models.ManyToManyField(UserProfile, related_name="invite_peoples")

    def __str__(self):
        return self.name_of_meeting


class Comment (models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    meeting = models.ForeignKey(
        Meeting, related_name='comments', on_delete=models.CASCADE)
    time_of_comment = models.DateTimeField(default=timezone.now)
    comment = models.TextField()
