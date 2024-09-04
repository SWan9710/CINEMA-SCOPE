from rest_framework import serializers
from ..models import Review
from .userSerializer import UserSerializer

class ReviewListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    like_count = serializers.IntegerField(source="liked_users.count", read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)
