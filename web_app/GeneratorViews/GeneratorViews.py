from datetime import timedelta
from dateutil import parser
from rest_framework.views import APIView
from rest_framework.response import Response

from web_app.serializers import GeneratorSerializer
from web_app.models import Person, Coordinate
from coordgen import get_difference_btw_dates, get_random_coordinate


class GeneratorView(APIView):
    """
    View to generate some coordinates
    """

    def post(self, request, format=None):
        """
        Generate coordinates
        """
        serializer = GeneratorSerializer(data=request.data)
        serializer.is_valid()
        start = parser.parse(serializer.data['start_date'])
        end = parser.parse(serializer.data['end_date'])
        latitude = serializer.data['latitude']
        longitude = serializer.data['longitude']
        person_id = serializer.data['person_id']
        person = Person.objects.get(pk=person_id)

        difference = get_difference_btw_dates(start, end)
        for _ in range(difference):
            point = get_random_coordinate(latitude, longitude)
            coordinate = Coordinate(person=person,
                                    latitude=point.latitude,
                                    longitude=point.longitude,
                                    created=start)
            coordinate.save()
            start += timedelta(minutes=1)
        return Response({"message": "Got some data!", "data": request.data})
