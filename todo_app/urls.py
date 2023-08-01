from django.urls import path
from .views import TodoListCreateAPIView, TodoUpdateAPIView

urlpatterns = [
    path('todos/', TodoListCreateAPIView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoListCreateAPIView.as_view(), name='todo-detail'),
    path('todos/update/<int:pk>/', TodoUpdateAPIView.as_view(), name='todo-update'),
]
