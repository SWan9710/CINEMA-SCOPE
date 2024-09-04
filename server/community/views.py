from django.shortcuts import get_object_or_404
from django.db.models import Count

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article, Comment
from .serializers.articles import ArticleListSerializer, ArticleSerializer
from .serializers.comments import CommentSerializer

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.annotate(
            comment_count = Count('comments', distinct=True),
            like_count = Count('liked_users', distinct=True)
        ).order_by('-pk')
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_or_update_or_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        if request.user == article.user:
            serializer = ArticleSerializer(instance=article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
    elif request.method == 'DELETE':
        if request.user == article.user:
            article.delete()
            data= {
                'delete':'삭제가 완료되었습니다.'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def like_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user
    if article.liked_users.filter(pk=user.pk).exists():
        article.liked_users.remove(user)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    else:
        article.liked_users.add(user)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

@api_view(['POST'])
def create_comment(request, article_pk):
    user = request.user
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user=user)
        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT':
        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                comments = article.comments.all()
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data)
    elif request.method == 'DELETE':
        if request.user == comment.user:
            comment.delete()
            comments = article.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)

@api_view(['POST'])
def like_comment(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    serializer = CommentSerializer(comment)
    if article.pk == serializer.data.get('article'):
        if comment.liked_users.filter(pk=request.user.pk).exists():
            comment.liked_users.remove(request.user)
        else:
            comment.liked_users.add(request.user)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)