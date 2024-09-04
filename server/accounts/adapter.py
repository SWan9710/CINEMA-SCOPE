import json
from allauth.account.adapter import DefaultAccountAdapter

#커스텀한 필드의 정보가 실제 데이터베이스에 반영되도록 저장.
class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        print('넌 하지?')
        data = form.cleaned_data
        user = super().save_user(request, user, form, False)
        profile_img = data.get("profile_img")
        genre_likes = data.get("genre_likes")
        if profile_img:
            user.profile_img = profile_img
        if genre_likes:
            user.genre_likes = genre_likes

        user.save()
        return user