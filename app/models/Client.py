from django.db import models
from django import forms


class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    nom_societe = models.CharField(max_length=50)


class ClientForm(forms.Form):
    class Meta:
        model = Client
        fields = ['nom', 'email', 'nom_societe', ]

