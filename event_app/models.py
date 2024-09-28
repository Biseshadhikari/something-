from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_country_guide = models.BooleanField(default=False)
    # You can add more fields if necessary.
