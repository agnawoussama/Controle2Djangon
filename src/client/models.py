from django.db import models

# Create your models here.
class Client(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    age = models.IntegerField()
    cin = models.CharField(max_length=12)
    dateEnrg = models.DateField(blank=True, null=True)






