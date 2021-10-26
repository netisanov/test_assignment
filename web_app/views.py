from .models import Person, Coordinate
from .serializers import PersonSerializer, CoordinateSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from coordgen import generator
from datetime import datetime, timedelta


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class CoordinateList(generics.ListAPIView):
    queryset = Coordinate.objects.all()
    serializer_class = CoordinateSerializer


class CoordinateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coordinate.objects.all()
    serializer_class = CoordinateSerializer



@api_view(['GET', 'POST'])
def coordinates_generator(request):
    if request.method == 'POST':
        data = request.data
        start = datetime.strptime(data.get('start_date'), "%Y-%m-%d %H:%M")
        end = datetime.strptime(data.get('end_date'), "%Y-%m-%d %H:%M")
        delta = end - start
        difference = delta.seconds // 60
        latitude = data.get("latitude")
        longitude = data.get("longitude")
        person_id = data.get("person_id")
        person = Person.objects.get(pk=person_id)
        while difference > 0:
            difference -= 1
            point = generator(latitude, longitude)
            latitude = point.latitude
            longitude = point.longitude
            coordinate = Coordinate(person=person,
                                    latitude=latitude,
                                    longitude=longitude,
                                    created=start)
            coordinate.save()
            start += timedelta(minutes=1)
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Generator"})


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'persons': reverse('person-list', request=request, format=format),
        'coordinates': reverse('coordinate-list', request=request, format=format),
    })