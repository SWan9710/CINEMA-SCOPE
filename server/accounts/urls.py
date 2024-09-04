from django.urls import path
from . import views

urlpatterns = [
    # 프로필 보기 및 수정
    path('profile/<username>/', views.profile_or_edit),
    # 유저 팔로우 요청
    path('<int:user_pk>/follow/', views.follow),
]
