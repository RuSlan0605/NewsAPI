from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.status import *
from post.models import CustomUser, Comment, Category, Post
from .permissions import (
    PostPermission,
    CommentPermission,
    CategoryPermission
)
from .serializers import (
    CustomUserSerializer,
    PostSerializer,
    CategorySerializer,
    CommentSerializer
)

class UserViewSet(ModelViewSet):
    
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]

class PostViewSet(ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [PostPermission]


class CommentView(APIView):

    permission_classes = [CommentPermission]

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)
    
class CommentDetailView(APIView):

    permission_classes = [CommentPermission]

    def get(self, request, pk=None):
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=HTTP_200_OK)
    
class CategoryView(APIView):

    permission_classes = [CategoryPermission]

    def get(self, request):
        categories = Category.objects.all()
        serilizer = CategorySerializer(categories, many=True)
        return Response(serilizer.data, status=HTTP_200_OK)
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class CategoryDetailView(APIView):

    permission_classes = [CategoryPermission]

    def get(self, request, pk=None):
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=HTTP_200_OK)
        





