from django.urls import path
from .views import *

urlpatterns = [
    path('', PostList.as_view(), name='posts_list'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail'),
    
    path('tags/', TagList.as_view(), name='tags_list'),
    path('tag/<str:slug>', TagDetail.as_view(), name='tag_detail')
]