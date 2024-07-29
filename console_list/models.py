import uuid

from django.db import models


class ConsoleItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    description = models.CharField(default=None, max_length=1200)
    company = models.CharField(default=None, max_length=100)
    image = models.CharField(default=None, max_length=100)
    original_price = models.FloatField(default=None)
    obtained = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"
