from .models import ToDoList, Item
from rest_framework import serializers


class ToDoListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDoList
        fields = ['id', 'name']


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['todolist', 'text', 'complete']
