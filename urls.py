# messaging/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # This is the root of the messaging app
    path('signup/', views.signup, name='signup'),  # Signup view
    path('login/', views.login_view, name='login'),  # Login view
    path('chatroom/', views.chatroom, name='chatroom'),  # Chatroom view
]