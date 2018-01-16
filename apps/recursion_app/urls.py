from django.conf.urls import url
from . import views           # This line is new!


urlpatterns = [
    url(r'^$', views.index),
    url(r'^collatz$', views.collatz),
    url(r'^fibonacci$', views.fibonacci),
    url(r'^gcf$', views.gcf),
    url(r'^qTree$', views.qTree),
    url(r'^repeated$', views.repeated),
    url(r'^repeatedWord$', views.repeatedWord),
    url(r'^reverseString$', views.reverseString),
    url(r'^rotateString$', views.rotateString),
    url(r'^subsets$', views.subsets),
    url(r'^sumArr$', views.sumArr),
    url(r'^sumOfTwoSquares$', views.sumOfTwoSquares),
]