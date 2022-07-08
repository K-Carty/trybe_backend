from rest_framework import serializers

from .models import Goal

class GoalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Goal
        fields = ('id', 'goal_description')