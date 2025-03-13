from rest_framework import serializers

class TweetSerializer(serializers.Serializer):
    name = serializers.CharField(
        required=True,
        max_length=10,
    )
    payload = serializers.CharField(
        max_length=180,
    )