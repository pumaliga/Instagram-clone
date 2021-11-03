from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from board.models import Post, CustomUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['avatar', 'username', 'first_name', 'last_name']


# class ProfileUpdateForm(ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ['avatar', 'username', 'first_name', 'last_name']


class PostCreate(ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'description']


class PostUpdateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'description']

