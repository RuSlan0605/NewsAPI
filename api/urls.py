from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, 
    PostViewSet,
    NewsView, 
    CommentView, 
    CategoryView,
    CategoryDetailView,
    CommentDetailView,
    NewsDetailView,
    )

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path('comments/', CommentView.as_view(), name='comments'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment'),
    path('news/', NewsView.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news'),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category')
] + router.urls