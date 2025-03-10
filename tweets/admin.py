from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Tweet, Like

# Register your models here.


@admin.register(Tweet)
class TweetAdmin(ModelAdmin):
    list_display = (
        'name',
        'user',
        'count_like'
    )

@admin.register(Like)
class LikeAdmin(ModelAdmin):
    list_display = (
        'reply',
        'select_tweet',
    )
