from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import Post, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    CRUD для пользователей.
    Используем встроенную модель User.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    CRUD для постов.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        """
        Добавляет/удаляет лайк для поста.
        """
        post = self.get_object()
        user = request.user
        # Если пользователь уже поставил лайк, удаляем его
        if user in post.likes.all():
            post.likes.remove(user)
            return Response({'status': 'лайк удален'}, status=status.HTTP_200_OK)
        else:
            post.likes.add(user)
            return Response({'status': 'лайк добавлен'}, status=status.HTTP_200_OK)

class CommentViewSet(viewsets.ModelViewSet):
    """
    CRUD для комментариев.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        """
        Добавляет/удаляет лайк для комментария.
        """
        comment = self.get_object()
        user = request.user
        if user in comment.likes.all():
            comment.likes.remove(user)
            return Response({'status': 'лайк удален'}, status=status.HTTP_200_OK)
        else:
            comment.likes.add(user)
            return Response({'status': 'лайк добавлен'}, status=status.HTTP_200_OK)
