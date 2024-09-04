from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import ProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET', 'PUT'])
def profile_or_edit(request, username):
    # 프로필 보기
    user = get_object_or_404(get_user_model(), username=username)
    if request.method == 'GET':
        serializer = ProfileSerializer(user)
        return Response(serializer.data)
    # 프로필 수정
    elif request.method == 'PUT':
        if request.user.is_authenticated:
            serializer = ProfileSerializer(data=request.data, instance=user)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

@api_view(['POST'])
def follow(request, user_pk):
    you = get_object_or_404(get_user_model(), pk=user_pk)
    me = request.user
    # 팔로우
    if you.followers.filter(pk=me.pk).exists():
        you.followers.remove(me)
    # 언팔로우
    else:
        you.followers.add(me)
    serializer = ProfileSerializer(you)
    return Response(serializer.data)