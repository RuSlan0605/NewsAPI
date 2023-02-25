from django.shortcuts import render
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth import get_user_model
from .serializers import PostSerializer
from .serializers import UserSerializer
from .models import Event
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

class PostViewSet(viewsets.ModelViewSet):

    permission_classes = (IsOwnerOrReadOnly, )
    queryset = Event.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser, )
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
   



