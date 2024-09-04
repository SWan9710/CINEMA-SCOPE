from django.urls import path
from . import views
app_name = 'community'

urlpatterns = [
    # 커뮤니티 게시글 list 받아오기(get), 생성(post)
    path('', views.article_list),
    # 커뮤니티 게시글 상세보기(get), 수정(put), 삭제(delete)
    path('<int:article_pk>/', views.article_detail_or_update_or_delete),
    # 좋아요 추가취소(post)
    path('<int:article_pk>/like/', views.like_article),
    # 게시글 댓글 추가(post)
    path('<int:article_pk>/comments/', views.create_comment),
    # 게시글 댓글 수정(put), 삭제(delete)
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comment_update_or_delete),
    # 게시글 댓글 좋아요 추가, 취소(post)
    path('<int:article_pk>/comments/<int:comment_pk>/like/', views.like_comment),
]
