from rest_framework import serializers
from ..models import Movie
from .reviewSerializer import ReviewListSerializer


class MovieListSerializer(serializers.ModelSerializer):

    reviews = ReviewListSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):

    reviews = ReviewListSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


