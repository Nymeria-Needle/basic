from django.db import models


# Create your models here.
class Students(models.Model):
    sid = models.IntegerField()
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30, null=True, blank=True)
    state = models.CharField(max_length=30, null=True, blank=True)
