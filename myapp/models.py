from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, username, password, is_staff=False, is_admin=False, is_active=True):
        if not username:
            raise ValueError('Users must have a username')
        if not password:
            raise ValueError('Users must enter a password')
        user = self.model(
            username=username
        )
        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.active = is_active
        user.save()
        return user

    def create_staffuser(self, username, password):
        user = self.create_user(
            username,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user


class User(AbstractBaseUser):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    username = models.CharField(max_length=150, unique=True)
    active = models.BooleanField(default=True)  # can login
    staff = models.BooleanField(default=False)  # staff not superuser
    admin = models.BooleanField(default=False)  # Superuser
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
