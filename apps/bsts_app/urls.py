from django.conf.urls import url
from . import views           # This line is new!


urlpatterns = [
    url(r'^$', views.index),
    url(r'^addNode$', views.addNode),
    url(r'^ceil$', views.ceil),
    url(r'^contains$', views.contains),
    url(r'^createBST$', views.createBST),
    url(r'^createBTnode$', views.createBTnode),
    url(r'^createFromArr$', views.createFromArr),
    url(r'^findAvg$', views.findAvg),
    url(r'^findMax$', views.findMax),
    url(r'^findMin$', views.findMin),
    url(r'^findSize$', views.findSize),
    url(r'^floor$', views.inOrder),
    url(r'^isBalanced$', views.isBalanced),
    url(r'^postOrder$', views.postOrder),
    url(r'^preOrder$', views.preOrder),
    url(r'^printAll$', views.printAll),
    url(r'^printDirections$', views.printDirections),
    url(r'^qBFS$', views.qBFS),
    url(r'^rBFS$', views.rBFS),
    url(r'^remove$', views.remove),
    url(r'^rRemove$', views.rRemove),
]