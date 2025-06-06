from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from .views import RegisterView


urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('signup/', RegisterView.as_view(template_name='users/signup.html'), name='signup'),
    path('password_reset/', PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
]