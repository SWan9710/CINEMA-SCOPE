from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    followings = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followers')
    profile_img = models.TextField(default='https://png.pngtree.com/png-vector/20191115/ourmid/pngtree-beautiful-profile-line-vector-icon-png-image_1990469.jpg', null=True)
    genre_likes = models.JSONField(default=dict, blank=True)