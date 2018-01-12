# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'sorts_app/index.html')

def bubble(request):
    return render(request, 'sorts_app/bubble.html')

def selection(request):
    return render(request, 'sorts_app/selection.html')

def rSelection(request):
    return render(request, 'sorts_app/rSelection.html')

def count(request):
    return render(request, 'sorts_app/count.html')

def merge(request):
    return render(request, 'sorts_app/merge.html')

def radix(request):
    return render(request, 'sorts_app/radix.html')

def rQuick(request):
    return render(request, 'sorts_app/rQuick.html')

def insertion(request):
    return render(request, 'sorts_app/insertion.html')
