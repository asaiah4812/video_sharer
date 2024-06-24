from django.urls import path
from .import views

urlpatterns = [
    path('login/', views.user_login, name="login"),
    path("signup/", views.user_register, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('<username>/', views.profile_view, name='userprofile'),
    path('profile/edit/', views.profile_edit, name='profile-edit')
]
