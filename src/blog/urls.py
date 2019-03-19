from django.urls import path
from .views import PostListView, PostDetailView
from . import views as blog_views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', blog_views.about, name='blog-about'),
]