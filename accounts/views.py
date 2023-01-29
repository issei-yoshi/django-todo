from django.contrib.auth.views import LoginView

class MyLoginView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True