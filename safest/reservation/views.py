from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from reservation.models import Chambre, Service, Universite
from reservation.serializers import (
    ChambreSerializer,
    ServiceSerializer,
    UniversiteSerializer,
)

# retrieves a list of all rooms


class ChambreListCreateAPIView(ListCreateAPIView):
    queryset = Chambre.objects.all()
    serializer_class = ChambreSerializer


class ChambreRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Chambre.objects.all()
    serializer_class = ChambreSerializer


# retrieves a list of all services


class ServiceListCreateAPIView(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


# retrieves a list of all university


class UniversiteListCreateAPIView(ListCreateAPIView):
    queryset = Universite.objects.all()
    serializer_class = UniversiteSerializer


class UniversiteRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Universite.objects.all()
    serializer_class = UniversiteSerializer
