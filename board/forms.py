from django.forms import ModelForm

from board.models import Post


class PostCreate(ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'description']

