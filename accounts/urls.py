from django.urls import path
from django.contrib.auth.views import LogoutView

from accounts.views import MyLoginView

urlpatterns = [
    path("login/", MyLoginView.as_view(), name="login"),
    path("loout/", LogoutView.as_view(), name="logout"),
]