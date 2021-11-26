from django.contrib.auth import get_user_model
'''imported CustomUser model via get_user_model which looks
to our AUTH_USER_MODEL config in settings.py'''
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)
