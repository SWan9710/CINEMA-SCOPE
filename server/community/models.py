from django.db import models
from django.conf import settings

# 커뮤니티 게시글
class Article(models.Model):
    # 작성자
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')
    # 제목
    title = models.CharField(max_length=50)
    # 내용
    content = models.TextField()
    # 작성시간
    created_at = models.DateTimeField(auto_now_add=True)
    # 수정시간
    updated_at = models.DateTimeField(auto_now=True)
    # 게시글 좋아요
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)

# 커뮤니티 게시글에 대한 댓글
class Comment(models.Model):
    # 작성자
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    # 게시글 정보(댓글이 누구의 게시글인지)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    # 댓글 내용
    content = models.TextField()
    # 작성시간
    created_at = models.DateTimeField(auto_now_add=True)
    # 업데이트 시간
    updated_at = models.DateTimeField(auto_now=True)
    # 댓글 좋아요
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments', blank=True)
