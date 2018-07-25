import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name
