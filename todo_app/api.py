# in book, this is done in views.py

from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import TodoSerializer
from .permissions import IsOwnerOrNoAccess
from .models import Todo

class TodoList(generics.ListCreateAPIView):
    # queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        queryset = Todo.objects.filter(user=self.request.user)
        return queryset


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsOwnerOrNoAccess, IsAuthenticated,)

    def get_queryset(self):
        queryset = Todo.objects.filter(user=self.request.user)
        return queryset
