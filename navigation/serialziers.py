from rest_framework import serializers
from .models import NavigationRecord, Vehicle


class NavigationRecordSerializer(serializers.ModelSerializer):
    vehicle_plate = serializers.ReadOnlyField(source='vehicle.plate')

    class Meta:
        model = NavigationRecord
        fields = ('latitude', 'longitude', 'vehicle_plate', 'nav_record_time')


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
