from rest_framework import generics
from .models import Tours, TourDetails
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import TourSerialzer, TourDetailsSerializer

class TourListCreateAPI(generics.ListCreateAPIView):
    queryset = Tours.objects.all()
    serializer_class = TourSerialzer

class TourListDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tours.objects.all()
    serializer_class = TourSerialzer


# List and create TourDetails
class TourDetailsListCreateAPI(generics.ListCreateAPIView):
    queryset = TourDetails.objects.all()
    serializer_class = TourDetailsSerializer

# Retrieve, update, and delete a single TourDetails instance
class TourDetailsDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = TourDetails.objects.all()
    serializer_class = TourDetailsSerializer

class TourDetailsByTitleAPI(APIView):
    def get(self, request, title_id):
        # Filter TourDetails by title_id (Tours ID)
        tour_details = TourDetails.objects.filter(title_id=title_id)
        serializer = TourDetailsSerializer(tour_details, many=True)
        return Response(serializer.data)
