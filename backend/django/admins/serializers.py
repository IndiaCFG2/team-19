from rest_framework import serializers
from .models import PolicyCreation
class PolicyCreationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=PolicyCreation
        fields = ('policyname', 'description')