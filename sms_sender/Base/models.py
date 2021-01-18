from django.db import models
from django.urls import reverse

# Create your models here.

class Message(models.Model):
    receptor = models.BigIntegerField(verbose_name='phone_number')
    message = models.TextField()

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse("detail", args=[self.id])
    