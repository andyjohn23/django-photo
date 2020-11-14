# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Image

# Create your views here.

def index(request):
    pics=Image.objects.all()
    return render(request, 'photo/index.html', {'pics':pics})