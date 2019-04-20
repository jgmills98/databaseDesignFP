from django.contrib import admin
from django.urls import path,include

from django.contrib.auth import views as auth_views

from user import views as user_views


urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='user/login.html'),name='login'),
    path('register/',user_views.register,name='register'),
    path('',include('search.urls'),name='home'),
    path('admin/', admin.site.urls),
]