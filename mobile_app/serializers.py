from rest_framework import serializers
from .models import AppUser

class AppUserSerializer(serializers.Serializer):

    user_name=serializers.CharField(read_only=True)
    google_play_account=serializers.URLField(read_only=True)


    def create(self, validated_data):
        return AppUser.objects.create(validated_data)


