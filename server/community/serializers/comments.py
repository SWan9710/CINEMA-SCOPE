from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Comment

class CommentSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')
            
    user = UserSerializer(read_only=True)
    liked_users = UserSerializer(read_only=True, many=True)
    class Meta:
        model = Comment
        fields = ('pk', 'user', 'liked_users', 'content', 'article',)
        read_only_fields = ('article', )