from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField(max_length=15,
                            required=True)
    telegram = forms.URLField(required=True)

    # add placeholder to forms data phone field and telegram
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = '@username'
        self.fields['phone'].widget.attrs.update({'placeholder': '97 123 45 67'})
        self.fields['telegram'].widget.attrs.update({'placeholder': 'https://t.me/username'})
  
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