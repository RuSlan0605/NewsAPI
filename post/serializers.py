from rest_framework import serializers
from post.models import Event
from django.contrib.auth import get_user_model

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            '__all__'
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)