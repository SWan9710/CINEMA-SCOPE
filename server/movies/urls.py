from django.urls import path
from . import views

urlpatterns = [
    # 장르 요청
    path('genres/', views.genres_list),
    # 전체 영화 요청
    path("movies/", views.movie_list),
    # 랜덤 영화 요청(Tinder 사용)
    path("movies/random/", views.movie_random_list),
    # 평점순 영화 요청(10개)
    path("movies/popularity/", views.movie_popularity),
    # 장르별 평점순 영화 요청(10개)
    path("movies/popularity/<int:genre>", views.movie_genre_popularity),
    # 개봉일 순으로 영화 요청(10개)
    path("movies/release_date/", views.movie_release_date),
    # 유저가 좋아요 한 영화 랜덤 20개 추천
    path("movies/userLikes/<int:userPK>/", views.movie_user_likes),
    # 영화 검색 요청
    path("movies/search/<str:search>/", views.movie_search),
    # 장르별 영화 검색 요청
    path("movies/search/<str:search>/<int:genre>/", views.movie_search_genre),
    # 영화 상세보기
    path("movies/<int:movie_pk>/", views.movie_detail),
    # 영화 좋아요 토글버튼(detail에서 사용)
    path("movies/<int:movie_pk>/toggleLikes/", views.movie_toggle_likes),
    # 영화 좋아요 요청
    path("movies/<int:movie_pk>/likes/", views.movie_likes),
    # 영화 좋아요 빼기 요청
    path("movies/<int:movie_pk>/dislikes/", views.movie_dislikes),
    # 영화에 대한 리뷰 생성
    path("movies/<int:movie_pk>/reviews/", views.movie_review_create),
    # 영화에 대한 리뷰 삭제
    path("movies/<int:movie_pk>/reviews/<int:review_pk>/", views.movie_review_detail),
    # 영화에 대한 리뷰 좋아요
    path("movies/<int:movie_pk>/reviews/<int:review_pk>/like/", views.movie_review_like),
]