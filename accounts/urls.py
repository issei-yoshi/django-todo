from django.urls import path
from django.contrib.auth.views import LogoutView

from accounts.views import MyLoginView, SignUpView

urlpatterns = [
    path("login/", MyLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
]