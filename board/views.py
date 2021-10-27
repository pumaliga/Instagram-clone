from django.utils import timezone
from django.views.generic import ListView, CreateView, DetailView

from board.forms import PostCreate
from board.models import Post


class BoardListView(ListView):
    queryset = Post.objects.all().filter(created__date__lte=timezone.now())    #?
    template_name = 'board.html'


class PostCreateView(CreateView):
    form_class = PostCreate
    model = Post
    template_name = 'post_create.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DetailPost(DetailView):
    model = Post
    template_name = 'post_detail.html'

