from django.conf.urls import url
from . import views           # This line is new!


urlpatterns = [
    url(r'^$', views.index),
    url(r'^bubble$', views.bubble),
    url(r'^selection$', views.selection),
    url(r'^rSelection$', views.rSelection),
    url(r'^count$', views.count),
    url(r'^merge$', views.merge),
    url(r'^radix$', views.radix),
    url(r'^rQuick$', views.rQuick),
    url(r'^insertion$', views.insertion),
]