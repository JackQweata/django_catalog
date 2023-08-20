from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class UserProfileForm(UserChangeForm):
    class Meta:
        models = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar',)


class PasswordResetForm(forms.Form):
    email = forms.EmailField(label='Email')
