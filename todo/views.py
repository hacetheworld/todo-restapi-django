from asyncio import Task
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from rest_framework import generics
from .serializers import TodoSerializer

from .models import *
# Create your views here.


def home(request):
    return render(request, "index.html")


# todos/views.py

class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
