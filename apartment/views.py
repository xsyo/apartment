from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, SAFE_METHODS

from .models import City, Apartment
from .serializers import CitySerializer, ApartmentSerializer, ListApartmentSerializer
from .filters import ApartmentFilter


class CityListAPIView(ListAPIView):

    queryset = City.objects.all()
    serializer_class = CitySerializer


class ApartmentListCreateAPIView(ListCreateAPIView):

    queryset = Apartment.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_class = ApartmentFilter

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return ListApartmentSerializer
        else:
            return ApartmentSerializer


class ApartmentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
