from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, joke, logout_view

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='jokes_app/login.html'), name='root'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='jokes_app/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('joke/', joke, name='joke'),
]
