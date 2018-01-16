# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'linkedlists_app/index.html')

def addBefore(request):
    return render(request, 'linkedlists_app/addBefore.html')

def addNode(request):
    return render(request, 'linkedlists_app/addNode.html')

def addToFront(request):
    return render(request, 'linkedlists_app/addToFront.html')

def createNode(request):
    return render(request, 'linkedlists_app/createNode.html')

def createSll(request):
    return render(request, 'linkedlists_app/createSll.html')

def deleteBack(request):
    return render(request, 'linkedlists_app/deleteBack.html')

def deleteNegatives(request):
    return render(request, 'linkedlists_app/deleteNegatives.html')

def findAll(request):
    return render(request, 'linkedlists_app/findAll.html')

def findSum(request):
    return render(request, 'linkedlists_app/findSum.html')

def findAvg(request):
    return render(request, 'linkedlists_app/findAvg.html')

def findFirst(request):
    return render(request, 'linkedlists_app/findFirst.html')

def findLength(request):
    return render(request, 'linkedlists_app/findLength.html')

def findMax(request):
    return render(request, 'linkedlists_app/findMax.html')

def findMin(request):
    return render(request, 'linkedlists_app/findMin.html')

def isPallindrome(request):
    return render(request, 'linkedlists_app/isPallindrome.html')

def rIsPallindrome(request):
    return render(request, 'linkedlists_app/rIsPallindrome.html')

def moveMinToFront(request):
    return render(request, 'linkedlists_app/moveMinToFront.html')

def nthFromLast(request):
    return render(request, 'linkedlists_app/nthFromLast.html')

def printAllNodes(request):
    return render(request, 'linkedlists_app/printAllNodes.html')

def removeFront(request):
    return render(request, 'linkedlists_app/removeFront.html')

def splitAt(request):
    return render(request, 'linkedlists_app/splitAt.html')

def addNodeValues(request):
    return render(request, 'linkedlists_app/addNodeValues.html')