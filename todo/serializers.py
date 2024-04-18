from rest_framework import serializers

from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=1000, required=True)

    def create(self, validated_data):
        return Todo.objects.create(title = validated_data.get('title'))
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance
    class Meta:
        model = Todo
        fields = "__all__"