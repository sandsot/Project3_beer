from django.urls import path
from account import views

urlpatterns = [
    path("login/", views.login),
    path("logout/", views.logout),
    path("mypage/", views.mypage),
    path("mybeer/", views.mybeer),
    path("signup/", views.signup),
]