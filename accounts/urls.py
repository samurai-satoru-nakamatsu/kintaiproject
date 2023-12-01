from django.urls import path
from . import views

urlpatterns = [
    path('/accounts/login', views.loginfunc, name='login'),
]
