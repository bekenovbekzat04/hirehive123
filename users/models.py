from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from users import choices


class UserManager(BaseUserManager):
    @staticmethod
    def _validate_user(email: str):
        if not email:
            raise ValueError('Users must have an email address')

    def create_user(self, email: str, password:str = None):
        self._validate_user(email=email)

        user = self.model(
            email=self.normalize_email(email),
            is_active=True
        )
        user.set_unusable_password()
        user.save()

        return user

    def create_superuser(self, email: str, password: str = None, username: str = None):
        self._validate_user(email=email)

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            is_active=True,
            is_staff=True,
            is_superuser=True
        )
        user.set_password(password)
        user.save()

        return user


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    user_type = models.CharField(
        max_length=10,
        choices=choices.UserTypeChoices.choices,
        blank=True,
        null=True,
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'
