from rest_framework import serializers
from .models import Thought

class ThoughtSerializer(serializers.Serializer):
    thought_date = serializers.CharField(max_length=30)
    thought = serializers.CharField(max_length=250)