from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie
from community.models import Article
from community.serializers.articles import ArticleSerializer
from movies.serializers.movieSerializer import MovieListSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer

class ProfileSerializer(serializers.ModelSerializer):
        
    like_articles = ArticleSerializer(many=True, read_only=True)
    articles = ArticleSerializer(many=True, read_only=True)
    like_movie = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'email', 'like_articles', 'articles', 'like_movie', 'genre_likes', 'followings', 'followers', 'profile_img')
        read_only_fields = ('followings', 'followers')

class CustomSignupSerializer(RegisterSerializer):
    profile_img = serializers.CharField(min_length=0)
    genre_likes = serializers.JSONField(default=dict)
    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['profile_img'] = self.validated_data.get('profile_img', '')
        data['genre_likes'] = self.validated_data.get('genre_likes', '')

        return data