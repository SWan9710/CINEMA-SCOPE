from rest_framework import serializers
from django.contrib.auth import get_user_model

from .comments import CommentSerializer
from ..models import Article
from ..models import Comment

class ArticleListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')
    
    comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    comment_count = serializers.IntegerField()
    like_count = serializers.IntegerField()
    class Meta:
        model = Article
        fields = ('pk', 'user', 'title', 'comments', 'content', 'comment_count', 'like_count', 'created_at', 'updated_at', 'liked_users')


class ArticleSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')
    
    user = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    liked_users = UserSerializer(read_only=True, many=True)
    class Meta:
        model = Article
        fields = ('pk', 'user', 'title', 'content', 'comments', 'liked_users', 'created_at', 'updated_at', 'liked_users')
