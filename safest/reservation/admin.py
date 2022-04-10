from django.contrib import admin

from .models import (
    TypeEtablissement,
    Etablissement,
    Universite,
    Universitetype,
    Chambre,
    Lit,
    TypeProprietaire,
    Proprietaire,
    Service,
    ReservationDortoire,
    ReservationService,
)

# Register your models here.
admin.site.register(TypeEtablissement)
admin.site.register(Etablissement)
admin.site.register(Universite)
admin.site.register(Universitetype)
admin.site.register(Chambre)
admin.site.register(Lit)
admin.site.register(TypeProprietaire)
admin.site.register(Proprietaire)
admin.site.register(Service)
admin.site.register(ReservationDortoire)
admin.site.register(ReservationService)
