from email.mime import application
from email.policy import default
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django.db import models
from django.utils.timezone import now


class Company(models.Model):
    class CompanyStatus(models.TextChoices):
        LAYOFFS = "Layoffs"
        HIRING_FREEZE = "Hiring Freeze"
        HIRING = "Hiring"

    name = models.CharField(max_length=30, unique=True)
    status = models.CharField(
        choices=CompanyStatus.choices, default=CompanyStatus.HIRING, max_length=30
    )
    last_update = models.DateTimeField(default=now, editable=True)
    application_link = models.URLField(blank=True)
    nodes = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return self.name
