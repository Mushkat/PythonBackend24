from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, UserSerializer
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from .permissions import IsOwnerOrReadOnly
from rest_framework.test import APIRequestFactory


class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(
            title='Test Post',
            content='Test Content',
            author=self.user
        )
        self.comment = Comment.objects.create(
            post=self.post,
            text='Test Comment',
            author=self.user
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.author.username, 'testuser')

    def test_comment_creation(self):
        self.assertEqual(self.comment.text, 'Test Comment')
        self.assertEqual(self.comment.post.title, 'Test Post')

class PostSerializerTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post_data = {
            'title': 'Test Post',
            'content': 'Test Content',
            'author': self.user.id
        }

    def test_post_serializer(self):
        serializer = PostSerializer(data=self.post_data)
        self.assertTrue(serializer.is_valid())

class CommentSerializerTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(
            title='Test Post',
            content='Test Content',
            author=self.user
        )
        self.comment_data = {
            'post': self.post.id,
            'text': 'Test Comment',
            'author': self.user.id
        }

    def test_comment_serializer_valid_data(self):
        serializer = CommentSerializer(data=self.comment_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['text'], 'Test Comment')

    def test_comment_serializer_invalid_data(self):
        invalid_data = {
            'post': self.post.id,
            'text': '',  # Пустое содержание
            'author': self.user.id
        }
        serializer = CommentSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('text', serializer.errors)

    def test_comment_serializer_create(self):
        self.comment_data = {
            'post': self.post.id,
            'text': 'Test Comment'
        }
        serializer = CommentSerializer(data=self.comment_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)  # Вывод ошибок
        comment = serializer.save(author=self.user)  # Назначьте автора вручную
        self.assertEqual(comment.text, 'Test Comment')
        self.assertEqual(comment.author, self.user)
        self.assertEqual(comment.post, self.post)

class UserSerializerTests(APITestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'password': 'testpass'
        }

    def test_user_serializer_valid_data(self):
        serializer = UserSerializer(data=self.user_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['username'], 'testuser')

    def test_user_serializer_invalid_data(self):
        invalid_data = {
            'username': '',
            'password': 'testpass'
        }
        serializer = UserSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('username', serializer.errors)

    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'password': 'testpass'
        }

    def test_user_serializer_create(self):
        serializer = UserSerializer(data=self.user_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        user = serializer.save()
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('testpass'))

class PostViewSetTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        self.url = reverse('post-list')

    def test_get_posts(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {'title': 'New Post', 'content': 'New Content'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class PermissionTests(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.other_user = User.objects.create_user(username='otheruser', password='testpass')
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)

    def test_owner_can_edit(self):
        request = self.factory.put('/posts/1/')
        request.user = self.user
        permission = IsOwnerOrReadOnly()
        self.assertTrue(permission.has_object_permission(request, None, self.post))

    def test_non_owner_cannot_edit(self):
        request = self.factory.put('/posts/1/')
        request.user = self.other_user
        permission = IsOwnerOrReadOnly()
        self.assertFalse(permission.has_object_permission(request, None, self.post))