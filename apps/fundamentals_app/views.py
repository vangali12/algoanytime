# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'fundamentals_app/index.html')

def isPalendrome(request):
    return render(request, 'fundamentals_app/isPalendrome.html')

def parensIsValid(request):
    return render(request, 'fundamentals_app/parensIsValid.html')

def censorship(request):
    return render(request, 'fundamentals_app/censorship.html')

def popFront(request):
    return render(request, 'fundamentals_app/popFront.html')