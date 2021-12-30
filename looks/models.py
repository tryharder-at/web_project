from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Apparel(models.Model):
    name = name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Look(models.Model):
    name = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True, blank=True)

    # Look-Apparel M-M
    apparels = models.ManyToManyField(Apparel)

    # Look-User Favourite M-M
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)

    def __str__(self):
        return self.name
