from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _
from .utils import *



class LowercaseEmailField(models.EmailField):
    """
    Override EmailField to convert emails to lowercase before saving.
    """
    def to_python(self, value):
        """
        Convert email to lowercase.
        """
        value = super(LowercaseEmailField, self).to_python(value)
        # Value can be None so check that it's a string before lowercasing.
        if isinstance(value, str):
            return value.lower()
        return value



class CustomUser(AbstractUser):
    email = LowercaseEmailField(null=True, blank=True)
    mobile_number = models.CharField(
        _("Mobile Number"), max_length=100, validators=[phone_validator],unique=True,
    )
    password = models.CharField(
        _("Password"), max_length=128, validators=[password_validator]
    )
    name = models.CharField(
        _("Full Name"), max_length=100, validators=[name_validator], null=True, blank=True
    )
    otp = models.CharField(max_length=8, null=True, blank=True)
    is_active = models.BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    username = None
    first_name = None
    last_name = None

    USERNAME_FIELD = "mobile_number"

    objects = CustomUserManager()

    def __str__(self):
        return str(self.mobile_number)
    
    def save(self, *args, **kwargs):
        """ This method is used to modify the password field
        converting text into hashed key"""
        if len(self.password) < 30:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
