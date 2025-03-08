from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
