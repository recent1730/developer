from django.urls import path
from .views import register
from django.contrib.auth.views import LoginView,LogoutView

app_name='authapp'
urlpatterns=[
    path('register/', register, name='register'),
    path('', LoginView.as_view(template_name='authapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='authapp/logout.html'), name='login'),
]
