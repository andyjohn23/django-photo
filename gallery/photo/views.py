# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Image
from django.views.generic import ListView

# Create your views here.

def index(request):
    photos=Image.objects.all()
    return render(request, 'photo/index.html', {'photos':photos})

class CategoryListView(ListView):
    template_name = 'photo/category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat':self.kwargs['category'],
            'images':Image.objects.filter(category__name=self.kwargs['category'])
        }
        return content