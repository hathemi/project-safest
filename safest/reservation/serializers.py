from rest_framework.serializers import ModelSerializer

from reservation.models import Chambre, Service, Universite


class ChambreSerializer(ModelSerializer):
    class Meta:
        model = Chambre
        fields = "__all__"


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"
        

class UniversiteSerializer(ModelSerializer):
    class Meta:
        model = Universite
        fields = "__all__"
