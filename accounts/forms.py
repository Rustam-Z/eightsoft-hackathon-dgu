from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField(max_length=15,
                            required=True)
    telegram = forms.URLField(required=True)

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            'email',
            'phone',
            'image',
            'telegram',
            'region',
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields