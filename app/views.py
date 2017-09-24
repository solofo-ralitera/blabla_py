# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from app import forms


# Create your views here.


def login(request):
    return render(request, 'app/login.html', locals())


def devi(request):
    return render(request,'devis/client.html')


def add(request):
    form = forms.ClientForm
    return render(request,'devis/client.html',{'form':form})
