from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    user_permissions_custom = models.ManyToManyField(
        Permission,
        blank=True
    )
    groups_custom = models.ManyToManyField(
        Group
    )
    is_api = models.BooleanField(default=False)

