from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from .models import City, District, Apartment, Image


class DistrictSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = District
        fields = ('id', 'name')


class CitySerializer(serializers.ModelSerializer):

    district = DistrictSerializer(many=True)

    class Meta:
        model = City
        fields = ('id', 'name', 'district')


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('id', 'img')


class ApartmentSerializer(WritableNestedModelSerializer):
    
    images = ImageSerializer(many=True, required=False)

    class Meta:
        model = Apartment
        fields = ('id', 'title', 'plot', 'floor', 'year_of_construction',
                    'room_count', 'address', 'price', 'district', 'avatar',
                    'description', 'created_at', 'updated_at', 'images')


class ListApartmentSerializer(WritableNestedModelSerializer):

    description = serializers.CharField(source='get_short_description', read_only=True)
    avatar = serializers.ImageField(source='avatar_thumbnail', read_only=True)

    class Meta:
        model = Apartment
        fields = ('id', 'title', 'avatar', 'year_of_construction', 
                    'room_count', 'price', 'description', 'created_at')


