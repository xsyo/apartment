from django_filters import rest_framework as filters

from .models import Apartment


class ApartmentFilter(filters.FilterSet):

    class Meta:
        model = Apartment
        fields = {
            'plot': ['in', 'gte', 'lte'],
            'floor': ['in', 'gte', 'lte'],
            'year_of_construction': ['in', 'gte', 'lte'],
            'room_count': ['in', 'gte', 'lte'],
            'price': ['gte', 'lte'],
            'created_at': ['gte', 'lte'], 
        }