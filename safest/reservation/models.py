from django.db import models
from django_extensions.db.fields import ShortUUIDField

# from django.contrib.auth.models import User
from django.conf import settings

User = settings.AUTH_USER_MODEL


class CommonInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]
        abstract = True


class TypeEtablissement(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Etablissement(CommonInfo):
    name = models.CharField(max_length=255, unique=True)
    tel = models.BigIntegerField(unique=True)
    fax = models.BigIntegerField(default=0)
    email = models.EmailField()
    nbre_etages = models.IntegerField()
    descripion = models.CharField(max_length=250)
    adresse = models.CharField(max_length=500)
    matricule_fiscale = models.CharField(max_length=500)
    type = models.ForeignKey(TypeEtablissement, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Universite(CommonInfo):
    name = models.CharField(max_length=255, unique=True)
    tel = models.BigIntegerField(unique=True)
    fax = models.BigIntegerField(default=0)
    email = models.EmailField()
    adresse = models.CharField(max_length=500)
    site_web = models.URLField(max_length=200, blank=True)
    type = models.ForeignKey(TypeEtablissement, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Universitetype(CommonInfo):
    id_universiate = models.ForeignKey(
        Universite,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Chambre(CommonInfo):
    id_etablissement = models.ForeignKey(
        Etablissement,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    etage = models.IntegerField()
    capacity = models.IntegerField()
    description = models.CharField(max_length=250)
    nbre_place_disponible = models.IntegerField()
    nbre_places_reservees = models.IntegerField()
    espace_m2 = models.FloatField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.prix) + ": DT"


class Lit(CommonInfo):
    id_chambre = models.ForeignKey(
        Chambre,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    code_lit = models.CharField(max_length=250)
    est_reserve = models.BooleanField(default=False)

    def __str__(self):
        return self.code_lit


class TypeProprietaire(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Proprietaire(CommonInfo):
    id = ShortUUIDField(primary_key=True, editable=False)
    id_etablissement = models.ForeignKey(
        Etablissement,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    type = models.ForeignKey(
        TypeProprietaire,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    nom = models.CharField(max_length=500)
    prenom = models.CharField(max_length=500)
    raison_social = models.CharField(max_length=500)
    email = models.EmailField(blank=True)
    tel_num = models.BigIntegerField(unique=True)

    def __str__(self):
        return self.raison_social


class Service(CommonInfo):
    id = ShortUUIDField(primary_key=True, editable=False)
    id_etablissement = models.ForeignKey(
        Etablissement,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    titre = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.titre


class ReservationDortoire(CommonInfo):
    id = ShortUUIDField(primary_key=True, editable=False)
    id_chambre = models.ForeignKey(
        Chambre,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    period = models.DurationField()
    id_client = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.period


class ReservationService(CommonInfo):
    id = ShortUUIDField(primary_key=True, editable=False)
    id_service = models.ForeignKey(
        Chambre,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    period = models.DurationField()
    id_client = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.period
