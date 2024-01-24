from rest_framework import serializers
from post.models import Category, Comment, CustomUser
from post.models import Post

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'password',
            'avatar',
            'is_staff',
        )
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            password = validated_data.pop('password')
            user = CustomUser.objects.create(**validated_data)
            user.set_password(password)
            return user

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'