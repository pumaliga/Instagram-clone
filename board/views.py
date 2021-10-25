from django.views.generic import ListView

from board.models import Post


class BoardListView(ListView):
    model = Post
    template_name = 'board.html'
