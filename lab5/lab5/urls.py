from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.lab5, name='lab5'),
    url(r'^info/(?P<pk>[0-9]+)$', views.info, name='info'),
]
