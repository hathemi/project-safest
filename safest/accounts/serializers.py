from django.contrib.auth import get_user_model
from rest_framework import serializers, validators

CustomUser = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    """
    We use this serializer for user registration. Most of the fields have
    `required=False`, but can be configured as needed. This serializer is used
    in `accounts.viewsets.CustomUserModelViewSet`.
    """

    tel = serializers.CharField(
        write_only=True,
        validators=[
            validators.UniqueValidator(
                message="This tel already exists", queryset=CustomUser.objects.all()
            )
        ],
    )
    password = serializers.CharField(write_only=True, required=False)
    nom = serializers.CharField(required=False)
    prenom = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)
    tel_verified = serializers.BooleanField(required=False)
    pays_code = serializers.CharField(required=False)
    conservatrice = serializers.BooleanField(required=False)
    alcoolique = serializers.BooleanField(required=False)
    accepte_animal = serializers.BooleanField(required=False)
    autre_details = serializers.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "nom",
            "prenom",
            "email",
            "password",
            "tel",
            "pays_code",
            "gender",
            "tel_verified",
            "conservatrice",
            "alcoolique",
            "accepte_animal",
            "autre_details",
        )


class CustomUserRetrieveSerializer(serializers.ModelSerializer):
    """
    We use this serializer to retrieve data of the currently logged in user.
    It is used in `accounts.views.UserRetrieveUpdateDestroyAPIView`
    """

    nom = serializers.CharField(required=False)
    prenom = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = (
            "nom",
            "prenom",
            "email",
            "tel",
            "gender",
            "conservatrice",
            "alcoolique",
            "accepte_animal",
            "autre_details",
            "id",
        )
