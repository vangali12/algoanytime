# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'bsts_app/index.html')

def addNode(request):
    return render(request, 'bsts_app/addNode.html')

def ceil(request):
    return render(request, 'bsts_app/ceil.html')

def contains(request):
    return render(request, 'bsts_app/contains.html')

def createBST(request):
    return render(request, 'bsts_app/createBST.html')

def createBTnode(request):
    return render(request, 'bsts_app/createBTnode.html')

def createFromArr(request):
    return render(request, 'bsts_app/createFromArr.html')

def findAvg(request):
    return render(request, 'bsts_app/findAvg.html')

def findMax(request):
    return render(request, 'bsts_app/findMax.html')

def findMin(request):
    return render(request, 'bsts_app/findMin.html')

def findSize(request):
    return render(request, 'bsts_app/findSize.html')

def floor(request):
    return render(request, 'bsts_app/floor.html')

def inOrder(request):
    return render(request, 'bsts_app/inOrder.html')

def isBalanced(request):
    return render(request, 'bsts_app/isBalanced.html')

def postOrder(request):
    return render(request, 'bsts_app/postOrder.html')

def preOrder(request):
    return render(request, 'bsts_app/preOrder.html')

def printAll(request):
    return render(request, 'bsts_app/printAll.html')

def printDirections(request):
    return render(request, 'bsts_app/printDirections.html')

def qBFS(request):
    return render(request, 'bsts_app/qBFS.html')

def rBFS(request):
    return render(request, 'bsts_app/rBFS.html')

def remove(request):
    return render(request, 'bsts_app/remove.html')

def rRemove(request):
    return render(request, 'bsts_app/rRemove.html')