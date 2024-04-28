from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, password, first_name="Admin", last_name="", **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        address = other_fields.get('address', '')
        phone = other_fields.get('phone', '')

        return self.create_user(email, first_name, last_name, address, phone, password, **other_fields)

    def create_user(self, email, first_name, last_name, address, phone, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name,
                          address=address, phone=phone, **other_fields)
        user.set_password(password)
        user.save()
        return user


class TripyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=127, blank=True, default='User')
    last_name = models.CharField(max_length=127, blank=True, default='')
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=63, null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.first_name + ' ' + self.last_name
