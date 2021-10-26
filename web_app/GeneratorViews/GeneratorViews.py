from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response

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
        data = request.data
        start = datetime.strptime(data.get('start_date'), "%Y-%m-%d %H:%M")
        end = datetime.strptime(data.get('end_date'), "%Y-%m-%d %H:%M")
        latitude = data.get("latitude")
        longitude = data.get("longitude")
        person_id = data.get("person_id")
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
