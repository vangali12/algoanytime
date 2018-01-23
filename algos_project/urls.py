"""algos_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^fundamentals/', include('apps.fundamentals_app.urls')),
    url(r'^stringsArrays/', include('apps.stringsarrays_app.urls')),
    url(r'^linkedLists/', include('apps.linkedlists_app.urls')),
    url(r'^queuesStacks/', include('apps.queuestacks_app.urls')),
    url(r'^recursion/', include('apps.recursion_app.urls')),
    url(r'^sorts/', include('apps.sorts_app.urls')),
    url(r'^bsts/', include('apps.bsts_app.urls')),
    url(r'^heaps/', include('apps.heaps_app.urls')),
    url(r'^graphs/', include('apps.graphs_app.urls')),
    url(r'^about/', include('apps.about_app.urls')),
    url(r'^$', include('apps.algos_app.urls')),
]
