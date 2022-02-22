from rest_framework import serializers
from django.contrib.auth import (get_user_model,)
from .models import Task

User=get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username')


class Task_get_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=('id','name','status','due_date')

class Task_update_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=('status',)
