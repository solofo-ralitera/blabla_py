from django.db import models


class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    nom_societe = models.CharField(max_length=50)

    def __init__(self):
        models.Model.__init__(self)

    #class Meta:
    #    verbose_name = 'CLient'

    def __str__(self):
        return self.nom



