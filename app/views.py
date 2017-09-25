# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from app.models import Client


# Create your views here.


def login(request):
    return render(request, 'app/login.html', locals())


def devi(request):
    return render(request,'app/devis/client.html')


def add(request):
    form = Client.ClientForm()
    return render(request, 'app/devis/client.html', {'form': form})
