from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_salesman = models.BooleanField(default=True)
    is_manager = models.BooleanField(default=False)
    is_courier = models.BooleanField(default=False)
    is_financeofficer = models.BooleanField(default=False)

