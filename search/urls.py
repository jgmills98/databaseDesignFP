from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="search-home"),
    path('test/',views.test,name="test-"),
    path('validate_username/', views.validate_username, name='get_response'),     
]