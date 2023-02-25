from django.urls import path
from .views import PostViewSet
from .views import UserViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='post')
urlpatterns = router.urls