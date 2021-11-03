from django.urls import path

from board.views import BoardListView, PostCreateView, DetailPost, Login, Registration, ProfileView, ProfileUpdateView, \
    Logout, PostDelete, PostUpdate

urlpatterns = [
    path('', BoardListView.as_view(), name='board'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Registration.as_view(), name='registration'),
    path('logout/', Logout.as_view(), name='logout'),
    path('new/', PostCreateView.as_view(), name='new'),
    path('post/<int:pk>/', DetailPost.as_view(), name='post-detail'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/update/<int:pk>/', ProfileUpdateView.as_view(), name='profile-update'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='post-delete'),
    path('post/update/<int:pk>/', PostUpdate.as_view(), name='post-update'),



]
