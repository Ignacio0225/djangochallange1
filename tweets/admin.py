from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Tweet, Like

# Register your models here.

class WordFilter(admin.SimpleListFilter):
    title = 'Filter  by Elon Musk'
    parameter_name = "name"
    def lookups(self, request, model_admin):
        return [
            ('elon','Elon Musk'),
        ]
    def queryset(self, request, tweets):
        name = self.value()
        if name:
            return tweets.filter(payload__contains=name)
        else:
            tweets





@admin.register(Tweet)
class TweetAdmin(ModelAdmin):
    list_display = (
        'name',
        'payload',
        'user',
        'count_like',

    )
    search_fields = (
        'payload',
        'user__username',
    )
    list_filter = (
        'created_at',
        WordFilter,

    )

@admin.register(Like)
class LikeAdmin(ModelAdmin):
    list_display = (
        'reply',
        'select_tweet',
        'user',
    )
    search_fields = (
        'user__username',
    )
    list_filter = (
        'created_at',
    )