from django.db import models
from django.contrib.auth.models import AbstractUser
from django_extensions.db.fields import ShortUUIDField
from reservation.models import Etablissement, Universite
from .managers import UserAccountManager
from django.utils.translation import gettext_lazy as _


# Create your models here.
USER_ROLES = [("Admin", "Admin"), ("Staff", "Staff")]


class CustomUser(AbstractUser):
    id = ShortUUIDField(primary_key=True, editable=False)
    username = None
    email = models.EmailField(_("email address"), blank=True)

    gender = models.CharField(
        max_length=140,
        null=True,
        choices=(("Male", "Masculin"), ("Female", "Feminin")),
    )

    nom = models.CharField(max_length=500, blank=True)
    prenom = models.CharField(max_length=500, blank=True)
    password = models.CharField(max_length=500, default='safe.student', editable=False)
    tel = models.BigIntegerField(unique=True)
    pays_code = models.IntegerField(blank=True)
    tel_verified = models.BooleanField(default=False, blank=True)
    pays_origine = models.CharField(max_length=500, blank=True)
    ville = models.CharField(max_length=500, blank=True)
    code_postal = models.IntegerField(default=0, blank=True)
    date_naissance = models.DateField(null=True, blank=True)
    langues = models.CharField(max_length=500, blank=True)
    niveau_education = models.CharField(max_length=500, blank=True)
    specialte = models.CharField(max_length=500, blank=True)
    est_occupant = models.BooleanField(default=True, blank=True)
    etablissement = models.ForeignKey(
        Etablissement,
        related_name="etablissement",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    universite = models.ForeignKey(
        Universite,
        related_name="universite",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    role = models.CharField(
        max_length=40, choices=USER_ROLES, default="Staff", blank=True
    )
    conservatrice = models.BooleanField(default=True, blank=True)
    alcoolique = models.BooleanField(default=False, blank=True)
    accepte_animal = models.BooleanField(default=False, blank=True)
    photo = models.ImageField(upload_to="users/photos", null=True, blank=True)
    autre_details = models.TextField(blank=True)
    date_joindre = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "tel"
    REQUIRED_FIELDS = []  # <- email and password are required by default

    objects = UserAccountManager()

    def __str__(self):
        return self.password
