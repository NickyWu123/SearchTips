from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Entries(models.Model):
     word = models.CharField(max_length=30)
     datetime=models.DateTimeField(default=timezone.now)
