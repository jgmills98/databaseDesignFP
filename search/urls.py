from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="search-home"),
    path('test/',views.test,name="test-"),
    path('result',views.result,name="view-result")    
]