from django.contrib.auth.views import LoginView


class UserLoginView(LoginView):
    template_name = 'login.html'
