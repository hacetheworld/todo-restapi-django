from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path('todos/', TodoListCreateView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoRetrieveUpdateDeleteView.as_view(),
         name='todo-retrieve-update-delete'),
]
