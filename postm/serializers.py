from rest_framework import serializers
from .models import *

class TodoSerializer(serializers.Serializer):
    title=serializers.CharField(required=False,allow_blank=True)
    desp=serializers.CharField(required=False,allow_blank=True)
    status=serializers.CharField(required=False,allow_blank=True)

    def create(self,validated_data):
        return Todo.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.desp=validated_data.get('desp',instance.desp)
        instance.status=validated_data.get('status',instance.status)
        instance.save()
        return instance
    