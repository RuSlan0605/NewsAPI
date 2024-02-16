from rest_framework import serializers
from post.models import Category, Comment
from post.models import Post, News
from users.models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

class CustomUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    is_staff = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(CustomUserSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data.get('password'))
        return super(CustomUserSerializer, self).update(instance, validated_data)

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'password',
        )

    @staticmethod
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

