# api/serializers.py
from rest_framework import serializers
from .models import User, Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate_status(self, value):
        allowed = ['Pending', 'In Progress', 'Completed']
        if value not in allowed:
            raise serializers.ValidationError(
                f"Status must be one of {allowed}"
            )
        return value
