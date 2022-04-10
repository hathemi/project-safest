# Define a custom user manager

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

# from validate_email import validate_email
# from validate_international_phonenumber import validate_international_phonenumber


class UserAccountManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, phone, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        # validate_international_phonenumber(phone)

        if not phone:
            raise ValueError(_("The phone must be set"))

        phone = self.normalize_phone(
            phone, country_code=extra_fields.get("country_code")
        )
        # email = self.normalize_email(email)
        # if not validate_email(email):
        #     raise ValueError(_('Invalid email set'))
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(phone, **extra_fields)
