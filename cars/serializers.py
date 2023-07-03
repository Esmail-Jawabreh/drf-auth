from rest_framework import serializers
from .models import Cars

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cars
        fields = ('id', 'owner', 'name', 'desc', 'created_at', 'updated_at')