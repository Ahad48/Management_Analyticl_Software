from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('register/', views.register, name='register'),
    path("sign_in/", LoginView.as_view(template_name="login/sign_in.html")),
    path('dashboard/', views.dashboard, name='dashboard'),
]