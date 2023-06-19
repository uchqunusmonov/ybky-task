from rest_framework import serializers
from .models import Resident, Availability, Room


class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name', 'type', 'capacity']


class RoomDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name', 'type', 'capacity']


class RoomAvailabilitySerializer(serializers.ModelSerializer):
    pass
