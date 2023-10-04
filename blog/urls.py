from django.urls import path
from django.views.decorators.cache import cache_page
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('', cache_page(60 * 15)(PostListView.as_view()), name='list_post'),
    path('post/<int:pk>/detail/', PostDetailView.as_view(), name='detail_post'),
    path('post/create/', PostCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='update_post'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete_post'),
]