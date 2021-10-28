from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import request
from django.utils import timezone
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from board.forms import PostCreate, RegistrationForm, ProfileUpdateForm
from board.models import Post, CustomUser


class Login(LoginView):
    template_name = 'login.html'
    success_url = '/'


class Registration(CreateView):
    form_class = RegistrationForm
    template_name = 'registration.html'
    success_url = '/'


class Logout(LoginRequiredMixin, LogoutView):
    next_page = '/'
    login_url = 'login/'


class BoardListView(LoginRequiredMixin, ListView):
    login_url = 'login/'
    queryset = Post.objects.all().filter(created__date__lte=timezone.now())    #?
    template_name = 'board.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login/'
    form_class = PostCreate
    model = Post
    template_name = 'post_create.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DetailPost(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'


class ProfileView(LoginRequiredMixin, DetailView):
    login_url = 'login/'
    model = CustomUser
    template_name = 'profile.html'
    # extra_context = {"posts": Post.objects.filter(author__username=self.request.user)}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_posts'] = Post.objects.filter(author__username=self.request.user)
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login/'
    model = CustomUser
    fields = ['avatar', 'username', 'first_name', 'last_name']
    # form_class = ProfileUpdateForm
    template_name = 'profile_update.html'

    def get_success_url(self):
        return f"/profile/{self.request.user.pk}/"


