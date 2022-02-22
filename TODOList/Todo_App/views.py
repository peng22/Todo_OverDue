from django.shortcuts import render
from rest_framework import generics

from .models import Task
from .serializers import(Task_get_Serializer,
                        Task_update_Serializer
                        )
from rest_framework.permissions import IsAuthenticated
from .permissions import Owner_Permission
# Create your views here.


class Task_List(generics.ListAPIView):
    serializer_class = Task_get_Serializer
    permission_classes=(IsAuthenticated,Owner_Permission,)
    filterset_fields=['status',]
    def get_queryset(self):
        owner = self.request.user
        return Task.objects.filter(owner=owner)


class Task_Details(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    permission_classes=(IsAuthenticated,Owner_Permission,)
    def get_serializer_class(self):
        if self.request.method=="GET":
            return Task_get_Serializer
        return Task_update_Serializer
