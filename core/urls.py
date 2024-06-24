from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<tag>/', views.home, name='category'),
    path('video/<str:pk>/', views.video_detail, name='video-detail')
]
