from rest_framework import serializers
from .models import Task, Contact
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
	user = serializers.ReadOnlyField(source='user.username')

	class Meta:
		model = Task
		fields = ('id' ,'title', 'user', )

class UserSerializer(serializers.ModelSerializer):
	tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

	class Meta:
		model = User
		fields = ('id', 'username', 'tasks')

class ContactSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contact
		fields = '__all__'