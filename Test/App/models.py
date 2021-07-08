from django.db import models

# Create your models here.

class Formation(models.Model):
    titre = models.CharField(max_length=30)
    logo = models.CharField(max_length=30)
    etat = models.BooleanField(default=False)