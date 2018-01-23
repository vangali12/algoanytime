from django.conf.urls import url
from . import views           # This line is new!


urlpatterns = [
    url(r'^$', views.index),
    url(r'^createSll$', views.createSll),
    url(r'^createNode$', views.createNode),
    url(r'^addNode$', views.addNode),
    url(r'^addBefore$', views.addBefore),
    url(r'^addToFront$', views.addToFront),
    url(r'^deleteBack$', views.deleteBack),
    url(r'^deleteNegatives$', views.deleteNegatives),
    url(r'^findAll$', views.findAll),
    url(r'^findSum$', views.findSum),
    url(r'^findAvg$', views.findAvg),
    url(r'^findFirst$', views.findFirst),
    url(r'^findLength$', views.findLength),
    url(r'^findMax$', views.findMax),
    url(r'^findMin$', views.findMin),
    url(r'^isPallindrome$', views.isPallindrome),
    url(r'^rIsPallindrome$', views.rIsPallindrome),
    url(r'^moveMinToFront$', views.moveMinToFront),
    url(r'^nthFromLast$', views.nthFromLast),
    url(r'^printAllNodes$', views.printAllNodes),
    url(r'^removeFront$', views.removeFront),
    url(r'^splitAt$', views.splitAt),
    url(r'^addNodeValues$', views.addNodeValues),
    url(r'^hasLoop$', views.hasLoop),    
]