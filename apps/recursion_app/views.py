# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'recursion_app/index.html')

def collatz(request):
    return render(request, 'recursion_app/collatz.html')

def fibonacci(request):
    return render(request, 'recursion_app/fibonacci.html')

def gcf(request):
    return render(request, 'recursion_app/gcf.html')

def qTree(request):
    return render(request, 'recursion_app/qTree.html')

def repeated(request):
    return render(request, 'recursion_app/repeated.html')

def repeatedWord(request):
    return render(request, 'recursion_app/repeatedWord.html')

def reverseString(request):
    return render(request, 'recursion_app/reverseString.html')

def rotateString(request):
    return render(request, 'recursion_app/rotateString.html')

def subsets(request):
    return render(request, 'recursion_app/subsets.html')

def sumArr(request):
    return render(request, 'recursion_app/sumArr.html')

def sumOfTwoSquares(request):
    return render(request, 'recursion_app/sumOfTwoSquares.html')

