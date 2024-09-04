from .models import Movie, Review
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers.genreSerializer import GenreListSerializer
from .serializers.movieSerializer import MovieListSerializer, MovieSerializer
from .serializers.reviewSerializer import ReviewListSerializer
from .models import Movie, Review, Genre

# 영화 장르 요청하기
@api_view(['GET'])
def genres_list(request):
    genres = get_list_or_404(Genre)
    serializers = GenreListSerializer(genres, many=True)
    return Response(serializers.data)

# 영화 리스트 받아오기
# 전체,평점순, 장르별 평점순, 신작, 내가 좋아요한 영화(없으면...... 안보여줭)
# 기본 뼈대는 전체
@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
# 평점순
@api_view(['GET'])
def movie_popularity(request):
    if request.method == 'GET':
        movies = Movie.objects.order_by('-vote_average')[0:20]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
# 장르별 평점 순
@api_view(['GET'])
def movie_genre_popularity(request, genre):
    if request.method == 'GET':
        movies = Movie.objects.filter(genres=genre).order_by('-vote_average')[0:20]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
# 신작
@api_view(['GET'])
def movie_release_date(request):
    if request.method == 'GET':
        movies = Movie.objects.order_by('-release_date')[0:20]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
# 유저가 좋아한 장르 영화 랜덤 20개 추천
@api_view(['GET'])
def movie_user_likes(request, userPK):
    if request.method == 'GET':
        movies = Movie.objects.filter(like_users=userPK).order_by('?')[0:20]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
# 영화 검색
@api_view(['GET'])
def movie_search(request, search):
    if request.method == 'GET':
        search = search.strip()
        movies = Movie.objects.filter(title__icontains=search).order_by('-vote_average')
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
# 장르별 검색
@api_view(['GET'])
def movie_search_genre(request, search, genre):
    if request.method == 'GET':
        search = search.strip()
        movies = Movie.objects.filter(genres=genre).filter(title__contains=search).order_by('-vote_average')
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

# 영화 상세보기
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie.reviews = movie.reviews.order_by('-pk')
    movie.save()
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

# 영화에 대한 좋아요 토글버튼
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_toggle_likes(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

# 영화에 대한 좋아요
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_likes(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if not movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.add(request.user)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

# 영화에 대한 좋아요 빼기 요청
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_dislikes(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

# 리뷰 생성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_review_create(reqeust, movie_pk):
    if reqeust.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = ReviewListSerializer(data=reqeust.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=reqeust.user)
            reviews = movie.reviews.all().order_by('pk')
            serializer = ReviewListSerializer(reviews, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
# 리뷰 삭제
# 로그인해야 사용할 수 있게 permission_class로 지정
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def movie_review_detail(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'DELETE':
        review.delete()
        reviews = movie.reviews.all().order_by('pk')
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
        
# 영화에 대한 리뷰 좋아요
@api_view(['POST'])
def movie_review_like(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewListSerializer(review)
    if movie.pk == serializer.data.get('movie'):
        if review.liked_users.filter(pk=request.user.pk).exists():
            review.liked_users.remove(request.user)
        else:
            review.liked_users.add(request.user)
        reviews = movie.reviews.all().order_by('pk')
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

# 랜덤으로 200개 가져오기 Tinder에서 쓸꺼
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_random_list(request):
    movies = Movie.objects.exclude(like_users=request.user.pk).order_by('?')[:200]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)