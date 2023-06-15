from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    user_permissions_custom = models.ManyToManyField(
        Permission,
        blank=True,
        related_query_name='customuser',
    )
    groups_custom = models.ManyToManyField(
        Group,
        related_query_name='customuser',
    )
    is_api = models.BooleanField(default=False)

