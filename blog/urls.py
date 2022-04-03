from . import views
from django.urls import path
from blog.views import *

urlpatterns = [
    path('blogs/', views.PostList.as_view(), name='index'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('add/', addBlog, name='addBlog'),
]