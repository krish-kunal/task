from django.db import models

# Create your models here.
class Save(models.Model):
    name=models.TextField(null=True, blank=True, default=None)
    json_field = models.TextField(null=True, blank=True, default=None)

