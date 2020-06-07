from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields=('name','status','label','due_date','date_created')
