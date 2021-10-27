from django.urls import path

from board.views import BoardListView, PostCreateView, DetailPost

urlpatterns = [
    path('', BoardListView.as_view(), name='board'),
    path('new/', PostCreateView.as_view(), name='new'),
    path('post/<int:pk>/', DetailPost.as_view(), name='post-detail'),

]
