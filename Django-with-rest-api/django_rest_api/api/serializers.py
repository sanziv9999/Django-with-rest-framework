from rest_framework import serializers
from .models import Tours, TourDetails

class TourSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Tours
        fields = '__all__'

class TourDetailsSerializer (serializers.ModelSerializer):
    class Meta:
        model = TourDetails
        fields = '__all__'