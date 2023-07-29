from django.urls import path
from .views import TodoListCreateAPIView

urlpatterns = [
    path('todos/', TodoListCreateAPIView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoListCreateAPIView.as_view(), name='todo-detail'),
]
