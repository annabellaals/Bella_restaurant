from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import Group


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        admin_group, _ = Group.objects.get_or_create(name='admin')
        user.groups.add(admin_group)
        user.save(using=self._db)
        return user