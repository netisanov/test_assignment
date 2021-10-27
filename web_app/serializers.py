from rest_framework import serializers
from django.utils import timezone

from .models import Person, Coordinate


class PersonSerializer(serializers.Serializer):
    id = serializers.HyperlinkedRelatedField(view_name='person-detail', read_only=True)
    name = serializers.CharField(max_length=40)
    surname = serializers.CharField(max_length=40, required=False)
    age = serializers.CharField(max_length=2, required=False)
    gender = serializers.ChoiceField(choices=Person.Gender.choices, default=Person.Gender.FEMALE)
    coordinates = serializers.HyperlinkedRelatedField(many=True, view_name='coordinate-detail', read_only=True)

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()
        return instance


class CoordinateSerializer(serializers.Serializer):
    person = serializers.HyperlinkedRelatedField(view_name='person-detail', read_only=True)
    latitude = serializers.FloatField(max_value=90, min_value=-90, required=False)
    longitude = serializers.FloatField(max_value=180, min_value=-180, required=False)
    created = serializers.DateTimeField(default=timezone.now)

    def create(self, validated_data):
        return Coordinate.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.person = validated_data.get('person', instance.name)
        instance.latitude = validated_data.get('latitude', instance.name)
        instance.longitude = validated_data.get('longitude', instance.age)
        instance.created = validated_data.get('created', instance.gender)
        instance.save()
        return instance


class GeneratorSerializer(serializers.Serializer):
    person_id = serializers.IntegerField()
    latitude = serializers.FloatField(max_value=90, min_value=-90)
    longitude = serializers.FloatField(max_value=180.0, min_value=-180)
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()


    def create(self, validated_data):
        return Coordinate.objects.create(**validated_data)

