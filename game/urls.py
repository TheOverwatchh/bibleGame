from django.urls import path 
from . import views

urlpatterns = [
    path('', views.gameLobby, name="gameLobby"),
    path('login', views.gameLogin, name='login'),
    path('register', views.gameRegister, name='register'),
    path('errorPage/<int:status>', views.errorPage, name='errorPage'),
    path('logout', views.logout_dj, name='logout')
]