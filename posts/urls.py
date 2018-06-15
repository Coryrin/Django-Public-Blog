from django.urls import path, re_path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostList.as_view(), name='list'),
    path('create/', views.CreatePostView.as_view(), name='create'),
    re_path(r'update/(?P<slug>[-\w]+)/', views.PostUpdate.as_view(), name='update'),
    re_path(r'delete/(?P<slug>[-\w]+)/', views.PostDelete.as_view(), name='delete'),
    re_path(r'(?P<slug>[-\w]+)/', views.post_detail, name='detail'),
]