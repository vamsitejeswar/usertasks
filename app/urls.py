from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserListCreateView.as_view()),
    path('tasks/', TaskListCreateView.as_view()),
    path('tasks/<int:pk>/', TaskDetailView.as_view()),
]