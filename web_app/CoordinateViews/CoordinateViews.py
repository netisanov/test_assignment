from rest_framework import generics

from web_app.models import Coordinate
from web_app.serializers import CoordinateSerializer


class CoordinateList(generics.ListAPIView):
    queryset = Coordinate.objects.all()
    serializer_class = CoordinateSerializer


class CoordinateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coordinate.objects.all()
    serializer_class = CoordinateSerializer
