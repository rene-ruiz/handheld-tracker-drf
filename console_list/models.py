from django.contrib.auth.models import User
from django.db import models
import uuid

class ConsoleItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    description = models.CharField(default=None, max_length=1200)
    company = models.CharField(default=None, max_length=100)
    image = models.CharField(default=None, max_length=100)
    original_price = models.FloatField(default=None)

    def __str__(self):
        return f"{self.name}"

class UserConsole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    console_item = models.ForeignKey(ConsoleItem, on_delete=models.CASCADE)
    date_obtained = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'console_item')

    def __str__(self):
        return f"{self.user.username} - {self.console_item.name}"
