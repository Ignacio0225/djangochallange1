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
        return self.name

    def count_like(self):
            return self.likes.count()



class Like(CommonModel):
    reply = models.CharField(
        max_length=10,
    )
    select_tweet = models.ForeignKey(
        'tweets.Tweet',
        null = True,
        blank = True,
        on_delete = models.SET_NULL,
        related_name='likes'
    )
    user = models.ForeignKey(
        'users.User',
        null=True,
        default='',
        on_delete= models.CASCADE,
        related_name='likes',
    )

    def __str__(self):
        return self.reply
