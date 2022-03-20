from rest_framework import serializers
from .models import Profile


class AuthorizationCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['phone']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
