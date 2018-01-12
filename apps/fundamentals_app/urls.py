from django.conf.urls import url
from . import views           # This line is new!


urlpatterns = [
    url(r'^$', views.index),
    url(r'^isPalendrome$', views.isPalendrome),
    url(r'^parensIsValid$', views.parensIsValid),
    url(r'^censorship$', views.censorship),
    url(r'^popFront$', views.popFront),
]