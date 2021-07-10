from django.db import models
from django.utils.html import escape

# Create your models here.

class Formation(models.Model):
    titre = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='images/')
    ETAT_CHOICES=[('activé','activé'),('désactivé','désactivé')]
    etat = models.CharField(max_length=30,choices=ETAT_CHOICES, default='activé')
    CATEGORIE_CHOICES=[('web','web'),('mobile','mobile'),('cloud','cloud')]
    categorie = models.CharField(max_length=30,choices=CATEGORIE_CHOICES, default='web')

