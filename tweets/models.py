from django.db import models
from django.db.models import ForeignKey
from common.models import CommonModel


# Create your models here.

class Tweet(CommonModel):
    name = models.CharField(
        max_length= 10,
    )
    payload = models.CharField(
        max_length= 180,
    )
    user = models.ForeignKey(
        'users.User',
        on_delete = models.CASCADE,
        related_name= 'tweets'
    )
    def __str__(self):
        return self.user

class Like(CommonModel):
    name = models.CharField(
        max_length=10,
    )
    user = models.ForeignKey(
        'users.User',
        null = True,
        blank = True,
        on_delete = models.SET_NULL,
        related_name='likes'
    )
    def __str__(self):
        return self.name
