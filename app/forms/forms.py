from django import forms
from app.models import Client


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('nom', 'email', 'nom_societe', )


