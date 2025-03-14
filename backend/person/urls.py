from django.urls import path
from .views import register_view, login_view, get_user_info, logout_view,check_login_status

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("user/", get_user_info, name="user_info"),
    path("logout/", logout_view, name="logout"),
     path("login_status/", check_login_status, name="login_status"),
]
