from django.urls import URLPattern, path
from . import views

# 为博客主页创建路径
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
