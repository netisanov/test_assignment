from rest_framework import serializers
from .models import Person, Coordinate


class PersonSerializer(serializers.ModelSerializer):
    coordinates = serializers.HyperlinkedRelatedField(many=True, view_name='coordinate-detail', read_only=True)
    id = serializers.HyperlinkedRelatedField(view_name='person-detail', read_only=True)

    class Meta:
        model = Person
        fields = ('id', 'name', 'surname', 'gender', 'age', 'coordinates')


class CoordinateSerializer(serializers.ModelSerializer):
    person = serializers.HyperlinkedRelatedField(view_name='person-detail', read_only=True)

    class Meta:
        model = Coordinate
        fields = ('id', 'person', 'created', 'latitude', 'longitude')

