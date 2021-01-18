from django.db import models

# Create your models here.

class Message(models.Model):
    receptor = models.BigIntegerField(verbose_name='phone_number')
    message = models.TextField()

    def __str__(self):
        return self.receptor